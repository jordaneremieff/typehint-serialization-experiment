from collections import namedtuple


from loamy.schema import Schema
from loamy.fields import String, Integer, Float, Number


class MockSchema(Schema):
    mystr = String()
    mybytes = String()
    myint = Integer()
    myfloat = Float()
    mynumber = Number()


def test_serialize_dict() -> None:
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


def test_serialize_object() -> None:
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


def test_serialize_namedtuple() -> None:

    MockModel = namedtuple("MockModel", ["user_id", "name"])

    class MockQuery:
        def get(self, user_id: int):
            return MockModel(name="jordan", user_id=user_id)

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
