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


def test_serializer() -> None:
    mock_schema = MockSchema(
        mystr="mystr", myint=1, mybytes=b"mybytes", myfloat=0.01, mynumber=1.0
    )

    data = {
        "mystr": "mystr",
        "myint": 1,
        "mybytes": b"mybytes",
        "myfloat": 0.01,
        "mynumber": 1.0,
    }

    mock_schema.serialize(data)

    assert mock_schema.serializer.data == {
        "mystr": "mystr",
        "myint": 1,
        "mybytes": b"mybytes",
        "myfloat": 0.01,
        "mynumber": 1.0,
    }


def test_object_serializer() -> None:
    class MockModel:
        user_id = 1
        name = "jordan"

    class MockQuery:
        def get(self, user_id: int):
            return MockModel()

    class UserSchema(Schema):
        user_id = Integer()
        name = String()

    user_id = 1
    schema = UserSchema(user_id=user_id)
    mock_user = MockQuery().get(user_id=user_id)
    schema.serialize(mock_user)
    schema.validate()
    assert schema.serializer.data == {"name": "jordan", "user_id": 1}


def test_serializer_json() -> None:
    mock_schema = MockSchema(
        mystr="mystr", myint=1, mybytes=b"mybytes", myfloat=0.01, mynumber=1.0
    )
    data = {
        "mybytes": b"mybytes1",
        "myfloat": 0.11,
        "myint": 2,
        "mynumber": 3.0,
        "mystr": "mystr2",
    }
    mock_schema.serialize(data)
    mock_schema.validate()

    json_s = '{"mybytes": "mybytes1", "myfloat": 0.11, "myint": 2, "mynumber": 3.0, "mystr": "mystr2"}'
    assert mock_schema.serializer.json == json_s
