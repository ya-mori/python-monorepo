from typing import List

from api.dto.user import CreateUserDto, UserDto, UserCreateStatusDto, UsersDto
from core.service.user_service import UserService


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_user(self, user_dto: CreateUserDto) -> UserCreateStatusDto:
        status = self.user_service.create_user(user_dto.name, user_dto.age)
        return UserCreateStatusDto(status=status)

    def find_all_user(self) -> UsersDto:
        users = [
            UserDto(id=user.id, name=user.name, age=user.age)
            for user in self.user_service.find_all_users()
        ]
        return UsersDto(users=users)

    def find_user_by_user_id(self, user_id: str) -> UserDto:
        user = self.user_service.find_user_by_id(user_id)
        return UserDto(id=user.id, name=user.name, age=user.age)
