from typing import List, Optional

from core.domain.user import User


class UserRepository:

    def find_all(self) -> List[User]:
        raise NotImplementedError

    def find_by_user_id(self, user_id: str) -> Optional[User]:
        raise NotImplementedError

    def insert_user(self, user: User) -> None:
        raise NotImplementedError

