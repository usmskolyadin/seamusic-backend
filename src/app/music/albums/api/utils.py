from dataclasses import dataclass

from src.domain.music.albums.api.schemas import BaseCurrentUser


# from src.domain.auth.users.core.service import BaseService


@dataclass
class CurrentUser(BaseCurrentUser):
    id: int


async def get_current_user() -> CurrentUser:
    return CurrentUser(id=1)
