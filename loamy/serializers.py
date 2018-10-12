from inspect import getmembers
from typing import Any, Union
import json


class Serializer:
    def __init__(self, fields: dict) -> None:
        """Serializer instance is created using the fields from the schema."""

        self.fields: dict = fields

    def __call__(self, data: Any, **kwargs) -> None:
        data = self.resolve(data)
        from pprint import pprint

        pprint(data)
        print(self.fields)

        for name, value in data.items():
            # Iterate the request data items, update the serializer field values.
            if name in self.fields:
                self.fields[name].value = value

    def resolve(self, data: dict) -> dict:
        """Resolve any nested field data that may exist in the serializer data."""
        data = self.convert(data)
        if data:
            for name, value in data.items():
                nested_data = self.convert(value)
                if nested_data is not None:
                    data[name] = nested_data

        return data

    def convert(self, data: Any) -> Union[dict, None]:
        """Convert serializer input data to dict."""
        if isinstance(data, (int, float, str, bytes)):
            return None

        if not isinstance(data, dict):

            # If the object can already be represented as a dict, then avoid the lookup
            # in the conversion process.
            if hasattr(data, "_asdict"):
                # Namedtuples support this method.
                data = data._asdict()

            elif not hasattr(data, "__getitem__"):
                # Inspect the members of the object and pull out any relevant fields.
                data = {
                    k: v
                    for k, v in getmembers(data)
                    if not k.startswith("__") and not k.endswith("__")
                }
        return data

    def get_dict(self) -> dict:
        """Return a dict containing the field values."""

        return {field.field_name: field.value for field in self.fields.values()}

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
