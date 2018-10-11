# loamy

![build](https://travis-ci.com/erm/loamy.svg?branch=master)
![black](https://img.shields.io/badge/code%20style-black-000000.svg)

An experiment into simple, framework-agnostic REST API serialization/de-serialization using type annotations.


## Usage

This may change quite a bit as time goes on:

```python3
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
```


## todo

- lots
