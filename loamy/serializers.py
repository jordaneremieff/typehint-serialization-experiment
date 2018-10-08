class Serializer:
    def __init__(self) -> None:
        self.fields: list = []

    def __call__(self, **kwargs) -> None:
        """Retrieve the fields and set the values to be validated."""
        for field_name, field_value in kwargs.items():
            field = getattr(self, field_name)
            field.field_value = field_value
            self.fields.append(field)

    def validate(self) -> None:
        """Call the validation method of each field."""
        for field in self.fields:
            field.validate()
