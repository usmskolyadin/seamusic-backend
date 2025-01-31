from typing import Annotated

from sqlalchemy import ARRAY, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from sqlalchemy import UUID as AlchemyUUID


"""
    Types for alchemy models
"""

StringArray = Mapped[Annotated[list[str], mapped_column(ARRAY(String))]]
IntegerArray = Mapped[Annotated[list[int], mapped_column(ARRAY(Integer))]]
UUIDArray = Mapped[Annotated[list[UUID], mapped_column(ARRAY(AlchemyUUID))]]
