import pytest

from loamy.fields import StrField, BytesField, IntField, FloatField, NumberField
from loamy.exceptions import ValidationError


def test_str_field():
    """Ensure only `bytes` or `str` types pass `StrField` validation."""
    myfield = StrField()

    myfield.field_value = "mystr"
    myfield.validate()

    myfield.field_value = b"mybytes"
    myfield.validate()

    myfield.field_value = 1
    with pytest.raises(ValidationError):
        myfield.validate()


def test_bytes_field():
    """Ensure only `bytes` type passes `BytesField` validation."""
    myfield = BytesField()

    myfield.field_value = b"mybytes"
    myfield.validate()

    myfield.field_value = 1
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.field_value = "mystr"
    with pytest.raises(ValidationError):
        myfield.validate()


def test_int_field():
    """Ensure only `int` type passes `IntField` validation."""
    myfield = IntField()

    myfield.field_value = 1
    myfield.validate()

    myfield.field_value = 0.01
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.field_value = "mystr"
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.field_value = b"mybytes"
    with pytest.raises(ValidationError):
        myfield.validate()


def test_float_field():
    """Ensure only `float` type passes `FloatField` validation."""
    myfield = FloatField()

    myfield.field_value = 0.01
    myfield.validate()

    myfield.field_value = 1
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.field_value = "mystr"
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.field_value = b"mybytes"
    with pytest.raises(ValidationError):
        myfield.validate()


def test_number_field():
    """Ensure only `int` and `float` types pass `NumberField` validation."""
    myfield = NumberField()

    myfield.field_value = 1
    myfield.validate()

    myfield.field_value = 0.01
    myfield.validate()

    myfield.field_value = "mystr"
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.field_value = b"mybytes"
    with pytest.raises(ValidationError):
        myfield.validate()
