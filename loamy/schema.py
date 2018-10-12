from inspect import getmembers
from typing import Any
from loamy.fields import Field
from loamy.serializers import Serializer


class Schema:

    serializer_class: Serializer = Serializer

    def __init__(self, field_name: str = None, **kwargs) -> None:
        """
        Build fields dict from the defined field types and assign the values.
        Schema types may also serve as nested field types.
        """
        self.field_name: str = field_name

        fields = self.get_fields()
        for name, field in fields.items():

            # A field name may be passed in the field constructor, otherwise assign its
            # default name.
            if field.field_name is None:
                field.field_name = name

        # Set any default values passed in the field constructor.
        for name, value in kwargs.items():
            field = fields[name]
            field.value = value

        self.fields: dict = fields
        self.serializer: Serializer = self.serializer_class(fields)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.__class__.__name__} fields={self.fields}>"

    def validate(self) -> None:
        """Call the validation method of each field."""

        for field in self.fields.values():
            field.validate()

    def serialize(self, data: Any, **kwargs) -> None:
        self.serializer(data, **kwargs)

    def get_fields(self) -> dict:
        """Get the fields defined on the schema."""
        fields = {k: v for k, v in getmembers(self) if isinstance(v, (Schema, Field))}

        return fields
