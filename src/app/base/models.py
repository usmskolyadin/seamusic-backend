from datetime import datetime, date

from sqlalchemy.orm import Mapped

from .types import IntegerArray, StringArray, UUIDArray

"""
    Class for extends
"""


class SocialActionExtend:
    viewers_ids: IntegerArray
    likers_ids: IntegerArray


class CreateUpdateExtend:
    created_at: Mapped[date]
    updated_at: Mapped[datetime]
