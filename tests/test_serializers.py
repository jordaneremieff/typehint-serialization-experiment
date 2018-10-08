from loamy.serializers import Serializer
from loamy.fields import StrField, BytesField, IntField, FloatField, NumberField


def test_serializer_fields():
    """
    Ensure base serializer behaviour allows for all field defintions and validates
    correctly typed parameters successfully.
    """

    class MySerializer(Serializer):
        mystr = StrField()
        myint = IntField()
        mybytes = BytesField()
        myfloat = FloatField()
        mynumber = NumberField()

    serializer = MySerializer()
    serializer(mystr="mystr", myint=1, mybytes=b"mybytes", myfloat=0.01, mynumber=1.0)
    serializer.validate()
