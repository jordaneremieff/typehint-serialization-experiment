from inspect import getmembers
from typing import Any
from loamy.fields import String, Integer, Float, Number
from loamy.serializers import Serializer


class Schema:

    serializer_class: Serializer = Serializer

    def __init__(self, **kwargs) -> None:
        """Build `fields` dict from the defined field types and assign the field values."""

        fields = self.get_fields()
        for name, field in fields.items():

            # Unless explicitly defined in the field definition, a field does not have
            # a name, assign it here if undefined.
            if field.name is None:
                field.name = name

        # Set any default values.
        for name, value in kwargs.items():
            field = fields[name]
            field.value = value

        self.fields: dict = fields
        self.serializer: Serializer = self.serializer_class(fields)

    def validate(self) -> None:
        """Call the validation method of each field."""

        for field in self.fields.values():
            field.validate()

    def serialize(self, data: Any, **kwargs) -> None:
        self.serializer(data, **kwargs)

    def get_fields(self) -> dict:
        """Get the fields defined on the schema."""
        fields = {
            k: v
            for k, v in getmembers(self)
            if isinstance(v, (String, Integer, Float, Number))
        }

        return fields
