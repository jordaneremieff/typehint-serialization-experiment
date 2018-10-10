from loamy.serializers import Serializer
from loamy.fields import String, Integer, Float, Number


class MockSerializer(Serializer):
    mystr = String()
    mybytes = String()
    myint = Integer()
    myfloat = Float()
    mynumber = Number()


def test_serializer_fields():
    """Ensure base serializer behaviour validates all field definitions."""

    serializer = MockSerializer(
        mystr="mystr", myint=1, mybytes=b"mybytes", myfloat=0.01, mynumber=1.0
    )
    serializer.validate()


class test_serializer_dict_fields:
    """Ensure dict args serialize and validate for all field definitions."""

    myargs = {
        "mystr": "mystr",
        "myint": 1,
        "mybytes": b"mybytes",
        "myfloat": 0.01,
        "mynumber": 1.0,
    }
    serializer = MockSerializer(**myargs)
    serializer.validate()


class test_serializer_to_dict:
    serializer = MockSerializer(
        mystr="mystr", myint=1, mybytes=b"mybytes", myfloat=0.01, mynumber=1.0
    )
    serializer.validate()
    assert serializer.get_dict() == {
        "mystr": "mystr",
        "myint": 1,
        "mybytes": b"mybytes",
        "myfloat": 0.01,
        "mynumber": 1.0,
    }


class test_serializer_to_json:
    serializer = MockSerializer(
        mystr="mystr", myint=1, mybytes=b"mybytes", myfloat=0.01, mynumber=1.0
    )
    serializer.validate()
    json_s = '{"mybytes": "mybytes", "myfloat": 0.01, "myint": 1, "mynumber": 1.0, "mystr": "mystr"}'
    assert serializer.get_json() == json_s
