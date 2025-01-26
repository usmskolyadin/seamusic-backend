from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.music.albums.api.schemas import (
    BaseSAlbumRequest,
    BaseSAlbumResponse,
    BaseSItemsRequest,
    BaseSPopularAlbumsResponse,
    BaseSArtistAlbumsResponse,
    BaseSArtistAlbumsRequest,
    BaseSUpdateAlbumCoverRequest,
    BaseSLikeAlbumRequest,
    BaseSCreateAlbumRequest,
    BaseSCreateAlbumResponse,
    BaseSUpdateAlbumRequest,
    BaseSUpdateAlbumResponse,
    BaseSDeleteAlbumRequest,
    BaseSUnlikeAlbumRequest,
    BaseCurrentUser,
)
from src.domain.music.albums.core.service import BaseService


@dataclass
class BaseRouter(ABC):
    @staticmethod
    @abstractmethod
    async def get_album(
        request: BaseSAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSAlbumResponse:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def get_popular_albums(
        page: BaseSItemsRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSPopularAlbumsResponse:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def get_artist_albums(
        request: BaseSArtistAlbumsRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSArtistAlbumsResponse:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def update_cover(
        request: BaseSUpdateAlbumCoverRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def like_album(
        request: BaseSLikeAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def unlike_album(
        request: BaseSUnlikeAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def create_album(
        request: BaseSCreateAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSCreateAlbumResponse:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def update_album(
        request: BaseSUpdateAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> BaseSUpdateAlbumResponse:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    async def delete_album(
        request: BaseSDeleteAlbumRequest,
        service: BaseService,
        current_user: BaseCurrentUser,
    ) -> None:
        raise NotImplementedError
