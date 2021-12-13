from functools import lru_cache

from api.controller.user_controller import UserController
from core.service.user_service import UserService
from core.utils.logger import get_logger
from database.repository.user_repository_impl import UserRepositoryImpl

logger = get_logger(__name__)


@lru_cache()
def get_user_controller() -> UserController:
    logger.info("call get_user_controller!")
    user_repository = UserRepositoryImpl()
    user_service = UserService(user_repository)
    controller = UserController(user_service)
    return controller
