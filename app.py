from loamy.schema import Schema
from loamy.fields import String, Integer

from starlette.endpoints import HTTPEndpoint
from starlette.applications import Starlette
from starlette.responses import JSONResponse


class MockModel:
    user_id = 1
    name = "jordan"


class MockQuery:
    def get(self, user_id: int):
        return MockModel()


class UserSchema(Schema):
    user_id = Integer()
    name = String()


app = Starlette()


@app.route("/{user_id}")
class APIEndpoint(HTTPEndpoint):
    async def get(self, request, user_id):

        schema = UserSchema(user_id=user_id)
        mock_user = MockQuery().get(user_id=user_id)
        schema.serialize(mock_user)
        schema.validate()
        data = schema.serializer.data

        return JSONResponse(data)
