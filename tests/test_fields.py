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
    """Test the `null` instance attribute using `Field` subclasses."""
    string_null = String(null=True)
    string_null.validate()

    string_not_null = String()
    string_not_null.value = ""

    with pytest.raises(ValidationError):
        string_not_null.validate()


def test_field_param_min_max():
    """Test the `min` and `max` instance attributes using `Field` subclasses."""
    string_min_max = String(min=1, max=10)
    string_min_max.value = "mystr"
    string_min_max.validate()

    string_min_max.value = b"mybytes"
    string_min_max.validate()

    integer_min_max = Integer(min=1, max=10)
    integer_min_max.value = 1
    integer_min_max.validate()

    float_min_max = Float(min=0.01, max=1.1)
    float_min_max.value = 1.00
    float_min_max.validate()

    number_min_max = Number(min=0.01, max=1.1)
    number_min_max.value = 1
    number_min_max.validate()

    string_min_max.value = "mystringistoolong"
    with pytest.raises(ValidationError):
        string_min_max.validate()

    integer_min_max.value = 10000
    with pytest.raises(ValidationError):
        integer_min_max.validate()

    float_min_max.value = 0.0001
    with pytest.raises(ValidationError):
        float_min_max.validate()

    number_min_max.value = 100000
    with pytest.raises(ValidationError):
        number_min_max.validate()


def test_field_param_name():
    """Test the `name` instance attribute."""
    field = String(null=True)
    assert field.field_name is None
    field.validate()
    assert field.field_name is None

    field = String(field_name="name", null=True)
    assert field.field_name == "name"
    field.validate()
    assert field.field_name == "name"


def test_field_param_value():
    """
    Test setting the value of the field when creating the instance to serve as a default.
    """

    field = String(value="myteststr")
    assert field.value == "myteststr"
    field.validate()
    assert field.value == "myteststr"


def test_field_repr():
    field = String(value="mystr", null=True, min=1, max=10)
    assert (
        repr(field)
        == "<String(field_name=None, value=mystr, max=10, min=1, null=True)>"
    )
