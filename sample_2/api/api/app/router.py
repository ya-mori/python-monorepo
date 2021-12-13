from typing import List

from fastapi import APIRouter

from api.app.injector import get_user_controller
from api.dto.user import UserDto, CreateUserDto, UserCreateStatusDto, UsersDto

router = APIRouter()


@router.get("/users")
async def get_all_users() -> UsersDto:
    controller = get_user_controller()
    return controller.find_all_user()


@router.get("/users/{user_id}")
async def get_user_by_id(user_id: str) -> UserDto:
    controller = get_user_controller()
    return controller.find_user_by_user_id(user_id)


@router.post("/users/create")
async def get_user_by_id(user: CreateUserDto) -> UserCreateStatusDto:
    controller = get_user_controller()
    return controller.create_user(user)
