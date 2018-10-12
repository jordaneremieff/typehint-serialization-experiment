# loamy

![build](https://travis-ci.com/erm/loamy.svg?branch=master)
![black](https://img.shields.io/badge/code%20style-black-000000.svg)

An experiment into REST API schemas and serialization. ***Work in progress.***

## Installation

You can install using `pip`:

```
pip install loamy
```

...but this is changing a lot at the moment, recommended to clone the repo locally:

```
git clone https://github.com/erm/loamy.git
```

## Usage

This may change quite a bit as time goes on:

```python
from loamy.schema import Schema
from loamy.fields import String, Integer


class MockUserModel:
    """
    A mock user model object that contains the query data for a test user.
    """

    def __init__(self, pk: int, username: str):
        self.pk: int = pk
        self.username: str = username
        self.profile: dict = {"metadata": "My user profile."}

    def __str__(self) -> str:
        return f"<MockUserModel: pk={self.pk}, username={self.username}>"


class MockUserQuery:
    """
    A mock query API to define test user data and a retrieval method.
    """

    users = {1: {"pk": 1, "username": "jordan"}}

    def get(self, pk: int) -> MockUserModel:
        user = self.users.get(pk)
        return MockUserModel(**user)


class Profile(Schema):
    """
    A user type schema that contains the field definitions for the model object.
    """

    metadata = String()


class User(Schema):
    """
    A user type schema that contains the field definitions for the model object.
    """

    pk = Integer()
    username = String()
    profile = Profile()


class UserSchema(Schema):
    """A loamy Schema that contains all of the fields."""

    user = User()


# Initialise the schema.
schema = UserSchema()

# Mock request example
request_data = {"pk": 1}
user_obj = MockUserQuery().get(request_data["pk"])


schema.serialize({"user": user_obj})
print(schema.serializer.data)
```

```shell
{'user': {'pk': 1, 'profile': {'metadata': 'My user profile.'}, 'username': 'jordan'}}
```

## todo

- lots
