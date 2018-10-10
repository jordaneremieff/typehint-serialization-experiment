import pytest

from loamy.fields import String, Integer, Float, Number
from loamy.exceptions import ValidationError


def test_string_field():
    """Ensure only `bytes` or `str` types pass `String` validation."""
    myfield = String()

    myfield.value = "mystr"
    myfield.validate()

    myfield2 = String()
    myfield2.value = b"mybytes"
    myfield2.validate()

    myfield3 = String()
    myfield3.value = 1
    with pytest.raises(ValidationError):
        myfield3.validate()


def test_integer_field():
    """Ensure only `int` type passes `Integer` validation."""
    myfield = Integer()

    myfield.value = 1
    myfield.validate()

    myfield.value = 0.01
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.value = "mystr"
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.value = b"mybytes"
    with pytest.raises(ValidationError):
        myfield.validate()


def test_float_field():
    """Ensure only `float` type passes `Float` validation."""
    myfield = Float()

    myfield.value = 0.01
    myfield.validate()

    myfield.value = 1
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.value = "mystr"
    with pytest.raises(ValidationError):
        myfield.validate()

    myfield.value = b"mybytes"
    with pytest.raises(ValidationError):
        myfield.validate()


def test_number_field():
    """Ensure only `int` and `float` types pass `Number` validation."""
    myfield = Number()
    myfield.value = 1
    myfield.validate()

    myfield2 = Number()
    myfield2.value = 0.01
    myfield2.validate()

    myfield3 = Number()
    myfield3.value = "mystr"
    with pytest.raises(ValidationError):
        myfield3.validate()

    myfield4 = Number()
    myfield4.value = b"mybytes"
    with pytest.raises(ValidationError):
        myfield4.validate()


def test_field_param_null():
    myfield = String(null=True)
    myfield.validate()

    myfield2 = String()
    myfield2.value = ""
    with pytest.raises(ValidationError):
        myfield2.validate()


def test_field_param_min():

    mystr = String(min=1)
    mystr.value = "mystr"
    mystr.validate()

    mybytes = String(min=1)
    mybytes.value = b"mybytes"
    mybytes.validate()

    myint = Integer(min=1)
    myint.value = 1
    myint.validate()

    mystr2 = String(min=10)
    mystr2.value = "mystr"
    with pytest.raises(ValidationError):
        mystr2.validate()

    myint2 = Integer(min=10)
    myint2.value = 1
    with pytest.raises(ValidationError):
        myint2.validate()
