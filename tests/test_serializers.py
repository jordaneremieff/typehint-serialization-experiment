import json

from loamy.serializers import Serializer
from loamy.fields import StrField, BytesField, IntField, FloatField, NumberField


def get_mock_serializer():
    class MySerializer(Serializer):
        mystr = StrField()
        myint = IntField()
        mybytes = BytesField()
        myfloat = FloatField()
        mynumber = NumberField()

    return MySerializer()


def test_serializer_fields():
    """
    Ensure base serializer behaviour allows for all field defintions and validates
    correctly typed parameters successfully.
    """

    serializer = get_mock_serializer()
    serializer(mystr="mystr", myint=1, mybytes=b"mybytes", myfloat=0.01, mynumber=1.0)
    serializer.validate()


class test_serializer_dict_fields:
    """Ensure dict args serialize and validate for all field defintions."""

    serializer = get_mock_serializer()

    myargs = {
        "mystr": "mystr",
        "myint": 1,
        "mybytes": b"mybytes",
        "myfloat": 0.01,
        "mynumber": 1.0,
    }
    serializer(**myargs)
    serializer.validate()


class test_serializer_to_dict:
    serializer = get_mock_serializer()
    serializer(mystr="mystr", myint=1, mybytes=b"mybytes", myfloat=0.01, mynumber=1.0)
    serializer.validate()
    assert serializer.get_dict() == {
        "mystr": "mystr",
        "myint": 1,
        "mybytes": b"mybytes",
        "myfloat": 0.01,
        "mynumber": 1.0,
    }


class test_serializer_to_json:
    serializer = get_mock_serializer()
    serializer(mystr="mystr", myint=1, mybytes=b"mybytes", myfloat=0.01, mynumber=1.0)
    serializer.validate()
    assert serializer.get_json() == json.dumps(
        {
            "mystr": "mystr",
            "myint": 1,
            "mybytes": "mybytes",
            "myfloat": 0.01,
            "mynumber": 1.0,
        }
    )
