from typing import List

from pydantic import BaseModel


class UserDto(BaseModel):
    id: str
    name: str
    age: int


class UsersDto(BaseModel):
    users: List[UserDto]


class CreateUserDto(BaseModel):
    name: str
    age: int


class UserCreateStatusDto(BaseModel):
    status: bool
