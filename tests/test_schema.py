from loamy.schema import Schema
from loamy.fields import String, Integer, Float, Number


class MockSchema(Schema):
    mystr = String()
    mybytes = String()
    myint = Integer()
    myfloat = Float()
    mynumber = Number()


def test_schema() -> None:
    """Ensure base mock_schema behaviour validates all field definitions."""

    mock_schema = MockSchema(
        mystr="mystr", mybytes=b"mybytes", myint=1, myfloat=0.01, mynumber=1.0
    )
    mock_schema.validate()


def test_schema_dict_args() -> None:
    """Ensure dict args serialize and validate for all field definitions."""

    myargs = {
        "mystr": "mystr",
        "mybytes": b"mybytes",
        "myint": 1,
        "myfloat": 0.01,
        "mynumber": 1.0,
    }
    mock_schema = MockSchema(**myargs)
    mock_schema.validate()
