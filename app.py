from loamy.serializers import Serializer
from loamy.fields import StrField, IntField


class MySerializer(Serializer):
    mystr = StrField()
    myint = IntField()


s = MySerializer()

s(mystr="test", myint=1)
s.validate()
