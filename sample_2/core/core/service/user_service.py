import uuid
from typing import List

from core.domain.user import User
from core.inerface.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, name: str, age: int) -> bool:
        new_user = User(id=str(uuid.uuid1()), name=name, age=age)
        self.user_repository.insert_user(user=new_user)
        return True

    def find_all_users(self) -> List[User]:
        return self.user_repository.find_all()

    def find_user_by_id(self, user_id: str) -> User:
        return self.user_repository.find_by_user_id(user_id)

