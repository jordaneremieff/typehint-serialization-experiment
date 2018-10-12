from inspect import getmembers
from typing import Any
import json


class Serializer:
    def __init__(self, fields: dict) -> None:
        """Serializer instance is created using the fields from the schema."""

        self.fields: dict = fields

    def __call__(self, data: Any, **kwargs) -> None:

        if not isinstance(data, dict):

            # If the object can already be represented as a dict, then avoid the lookup
            # in the conversion process.
            if hasattr(data, "_asdict"):

                # Namedtuples support this method.
                data = data._asdict()
            elif not hasattr(data, "__getitem__"):

                # Inspect the members of the object and pull out any relevant fields.
                data = {k: v for k, v in getmembers(data) if k in self.fields}

        for name, value in data.items():

            # Iterate the request data items, update the serializer field values.
            if name in self.fields:
                self.fields[name].value = value

    def get_dict(self) -> dict:
        """Return a dict containing the field values."""

        return {field.name: field.value for field in self.fields.values()}

    def get_json(self) -> str:
        """Return a JSON-dict containing the field values."""

        json_dict = self.data.copy()
        for field_name, field_value in json_dict.items():
            if isinstance(field_value, bytes):
                json_dict[field_name] = field_value.decode("latin-1")
        return json.dumps(json_dict)

    @property
    def data(self) -> dict:
        return self.get_dict()

    @property
    def json(self) -> dict:
        return self.get_json()
