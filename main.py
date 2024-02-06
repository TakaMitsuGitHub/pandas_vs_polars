from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    is_active: bool
    email: str



user_data = {"id": 123, "name": "Alice", "is_active": True, "email": "alice@example.com"}
user = User(**user_data)
print(user)


try:
    invalid_user_data = {"id": "not a number", "name": "Alice", "is_active": True, "email": "alice@example.com"}
    user = User(**invalid_user_data)
except ValidationError as e:
    print(e)
