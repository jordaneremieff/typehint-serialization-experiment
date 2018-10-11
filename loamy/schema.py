from inspect import getmembers
from loamy.fields import String, Integer, Float, Number
from loamy.serializers import Serializer


class Schema:

    serializer_class: Serializer = Serializer

    def __init__(self, **kwargs) -> None:
        """Build `fields` dict from the defined field types and assign the field values."""

        fields = self.get_fields()

        for name, value in kwargs.items():
            field = fields[name]
            field.value = value

            # Unless explicitly defined in the field definition, a field does not have
            # a name, assign it here if undefined.
            if field.name is None:
                field.name = name

        self.fields: dict = fields
        self.serializer: Serializer = None

    def validate(self) -> None:
        """Call the validation method of each field."""

        for field in self.fields.values():
            field.validate()

    def serialize(self) -> None:
        self.serializer = self.serializer_class(self.fields)

    def get_fields(self) -> dict:
        """Get the fields defined on the schema."""
        fields = {
            k: v
            for k, v in getmembers(self)
            if isinstance(v, (String, Integer, Float, Number))
        }

        return fields
