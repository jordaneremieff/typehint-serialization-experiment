from typing import Any, Union
from loamy.exceptions import ValidationError


class Field:
    def __init__(
        self,
        name: str = None,
        max: int = None,
        min: int = None,
        null: bool = False,
        value: Any = None,
    ):
        self.name: str = name
        self.max: int = max
        self.min: int = min
        self.null: bool = null
        self.types: list = []

        # Get the annotation for the field value to use when setting the allowed types.
        self.annotation = self.__annotations__["value"]

        # A subclass will define the annotation to apply to the value. This value will
        # also serve as an optional default.
        self.value: self.annotation = value

    def __repr__(self) -> str:
        args = ", ".join(
            [
                f"{key}={getattr(self, key)}"
                for key in ("name", "value", "max", "min", "null")
            ]
        )
        return f"<{self.__class__.__name__}({args})>"

    def set_types(self, annotation: Any) -> None:
        """Recursively unpack the annotation and extend the accepted field types."""

        if hasattr(annotation, "__args__"):
            params = annotation.__args__
            self.set_types(params)
        else:
            self.types.extend(annotation)

    def validate(self) -> None:
        """Validate the provided field value."""

        if self.value in (None, ""):

            # Ensure that the value of the field passes the nullable test.
            if not self.null:
                raise ValidationError("Undefined value for non-nullable field")
            else:

                # Nothing more to do, nullable field value is allowed.
                return

        # If the annotation doesn't have an `__args__` attribute (ie: not a Union[...]),
        # then append the type and continue. Otherwise there are multiple types that
        # must be unpacked.
        if not hasattr(self.annotation, "__args__"):
            self.types.append(self.annotation)
        else:
            self.set_types(self.annotation)

        # Ensure the field's value is an acceptable type.
        if not isinstance(self.value, tuple(self.types)):
            raise ValidationError(f"{self.value} is not of type {self.types}")

        # Validate the minimums and maximums for the type, if defined.
        if self.max is not None or self.min is not None:

            # String type size is determined by the length of the field value.
            if isinstance(self.value, (str, bytes)):
                size = len(self.value)
            else:
                size = self.value

            if self.min is not None and not size >= self.min:
                raise ValidationError(
                    f"Invalid minimum: {size} is less than {self.min}"
                )
            elif self.max is not None and not size <= self.max:
                raise ValidationError(
                    f"Invalid maximum: {size} is greater than {self.max}"
                )


class String(Field):
    """A field for `str` and `bytes` types."""

    value: Union[str, bytes] = None


class Integer(Field):
    """A field for only `int` type."""

    value: int = None


class Float(Field):
    """A field for only `float` type."""

    value: float = None


class Number(Field):
    """A field for both `int` and `float` types."""

    value: Union[int, float] = None
