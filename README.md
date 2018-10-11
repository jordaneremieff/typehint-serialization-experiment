# loamy

![build](https://travis-ci.com/erm/loamy.svg?branch=master)
![black](https://img.shields.io/badge/code%20style-black-000000.svg)

An experiment into REST API schemas and serialization.


## Usage

This may change quite a bit as time goes on:

```python
from loamy.schema import Schema
from loamy.fields import String, Integer


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
print(schema.serializer.data)
```

```shell
{'name': 'jordan', 'user_id': 1}
```

## todo

- lots
