import json
from inspect import getmembers
from loamy.fields import String, Integer, Float, Number


class Serializer:
    def __init__(self, **kwargs) -> None:
        """Build `fields` dict from the defined field types and assign the field values."""
        self.fields: dict = self.get_field_types()
        for name, value in kwargs.items():
            field = self.fields[name]
            field.value = value
            # Unless explicitly defined in the field definition, a field does not have
            # a name. Assign it here if it is `None`.
            if field.name is None:
                field.name = name

    def validate(self) -> None:
        """Call the validation method of each field."""
        for field in self.fields.values():
            field.validate()

    def get_field_types(self):
        """Get the fields defined on the serializer instance."""
        # todo: Build typelist elsewhere to allow custom type defintions?
        attrs = {
            k: v
            for k, v in getmembers(self)
            if isinstance(v, (String, Integer, Float, Number))
        }
        return attrs

    def get_dict(self) -> dict:
        """Return a dict containing the field values."""
        return {field.name: field.value for field in self.fields.values()}

    def get_json(self) -> str:
        """Return a JSON-dict containing the field values."""
        field_dict = self.get_dict()
        for field_name, field_value in field_dict.items():
            if isinstance(field_value, bytes):
                field_dict[field_name] = field_value.decode("latin-1")
        return json.dumps(field_dict)
