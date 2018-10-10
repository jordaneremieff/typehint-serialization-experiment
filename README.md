# loamy

An experiment into simple, framework-agnostic REST API serialization/de-serialization using type annotations.


## Example

This is very likely to change a bit:

```python3
    from loamy.serializers import Serializer
    from loamy.fields import String, Integer, Float, Number


    class MySerializer(Serializer):
        mystr = String(min=1, max=10)
        mynullstr = String(null=True)
        mybytes = String()
        myint = Integer(min=1)
        myfloat = Float(min=0.001)
        mynumber = Number()


    request_data = {
        "mystr": "mystr",
        "myint": 1,
        "mybytes": b"mybytes",
        "myfloat": 0.01,
        "mynumber": 1.0,
    }

    s = MySerializer(**request_data)
    s.validate()
```


## todo

- Determine how to handle validation state transitions
- More complex JSON serializer
- Nested/complex objects
- App examples