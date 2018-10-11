from loamy.schema import Schema
from loamy.fields import String, Integer, Float, Number


class MySchema(Schema):
    mystr = String(min=1, max=10)
    mynullstr = String(null=True)
    mybytes = String()
    myint = Integer(min=1)
    myfloat = Float(min=0.001)
    mynumber = Number(value=1)


request_data = {
    "mystr": "mystr",
    "myint": 1,
    "mybytes": b"mybytes",
    "myfloat": 0.01,
    "mynumber": 1.0,
}

s = MySchema(**request_data)
s.validate()
s.serialize()
print(s.serializer.data)
print(s.serializer.json)
