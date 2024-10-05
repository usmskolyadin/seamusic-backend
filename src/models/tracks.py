from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.base import Base
from src.models.albums import Album

artist_profile_track_association = Table(
    "artist_profile_track_association",
    Base.metadata,
    Column("artist_profile_id", Integer, ForeignKey("artist_profiles.id"), primary_key=True),
    Column("track_id", Integer, ForeignKey("tracks.id"), primary_key=True),
)


class Track(Base):
    __tablename__ = "tracks"
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    picture_url: Mapped[str] = mapped_column(nullable=True)
    file_url: Mapped[str] = mapped_column(nullable=False)
    tags_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), nullable=True)
    album_id: Mapped[int] = mapped_column(ForeignKey("albums.id"))
    album: Mapped["Album"] = relationship("Album", foreign_keys=[album_id])  # type: ignore[name-defined]  # noqa: F821
    tags: Mapped[list["Tag"]] = relationship("Tag", foreign_keys=[tags_id])  # type: ignore[name-defined]  # noqa: F821
