from typing import List, Dict, Optional

from core.domain.user import User
from core.inerface.user_repository import UserRepository


class UserRepositoryImpl(UserRepository):
    storage: Dict[str, User] = dict()

    def find_all(self) -> List[User]:
        return [v for _, v in self.storage.items()]

    def find_by_user_id(self, user_id: str) -> Optional[User]:
        return self.storage.get(user_id)

    def insert_user(self, user: User) -> None:
        self.storage[user.id] = user
