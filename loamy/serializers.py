import json


class Serializer:
    def __init__(self) -> None:
        self.fields: list = []

    def __call__(self, **kwargs) -> None:
        """Retrieve the fields and set the values to be validated."""
        for field_name, field_value in kwargs.items():
            field = getattr(self, field_name)
            field.field_value = field_value
            field.field_name = field_name
            self.fields.append(field)

    def validate(self) -> None:
        """Call the validation method of each field."""
        for field in self.fields:
            field.validate()

    def get_dict(self) -> dict:
        """Return a dict containing the field values."""
        return {field.field_name: field.field_value for field in self.fields}

    def get_json(self) -> str:
        """Return a JSON-dict containing the field values."""
        field_dict = self.get_dict()
        for field_name, field_value in field_dict.items():
            if isinstance(field_value, bytes):
                field_dict[field_name] = field_value.decode("latin-1")
        return json.dumps(field_dict)
