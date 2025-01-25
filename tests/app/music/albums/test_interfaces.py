from datetime import date, datetime
from typing import Literal, Callable

import pytest

from src.app.music.albums.interfaces.da.dao import PostgresDAOImplementation, get_postgres_dao_implementation
from src.app.music.albums.interfaces.da.models import Album


class TestPostgresDAOImplementation:
    @pytest.fixture(scope='session')
    def dao_impl_factory(self) -> Callable[[], PostgresDAOImplementation]:
        return get_postgres_dao_implementation

    @pytest.fixture(scope='session')
    def album_title(self) -> str:
        return 'title'

    @pytest.fixture(scope='session')
    def album_type(self) -> Literal['album', 'single']:
        return 'single'

    @pytest.fixture(scope='session')
    def album_created_at(self) -> date:
        return date.today()

    @pytest.fixture(scope='session')
    def album_updated_at(self) -> datetime:
        return datetime.now()

    @pytest.fixture(scope='session')
    def album_viewers_ids(self) -> list[int]:
        return [1]

    @pytest.fixture(scope='session')
    def album_likers_ids(self) -> list[int]:
        return [1]

    @pytest.fixture(scope='session')
    def album_artists_ids(self) -> list[int]:
        # return [artist['id']]
        return []

    @pytest.fixture(scope='session')
    def album_tracks_ids(self) -> list[int]:
        # return [track['id']]
        return []

    @pytest.fixture(scope='session')
    def album_tags(self) -> list[str]:
        # return [tag_name]
        return []

    @pytest.fixture(scope='session')
    def artist_id(self) -> int:
        return 1

    @pytest.fixture(scope='session')
    def album_picture_url(self) -> str:
        return 'ftp://picture.png'

    @pytest.fixture(scope='session')
    def album_description(self) -> str:
        return 'description'

    @pytest.fixture(scope='session')
    def album(
        self,
        album_title: str,
        album_type: Literal['album', 'single'],
        album_created_at: date,
        album_updated_at: datetime,
        album_viewers_ids: list[int],
        album_likers_ids: list[int],
        album_artists_ids: list[int],
        album_tracks_ids: list[int],
        album_tags: list[str],
        album_picture_url: str | None,
        album_description: str | None,
    ) -> dict:
        return {
            'id': None,
            'title': album_title,
            'description': album_description,
            'picture_url': album_picture_url,
            'album_type': album_type,
            'created_at': album_created_at,
            'updated_at': album_updated_at,
            'viewers_ids': album_viewers_ids,
            'likers_ids': album_likers_ids,
            'artists_ids': album_artists_ids,
            'tracks_ids': album_tracks_ids,
            'tags': album_tags,
        }

    async def test_create_album(
        self,
        album_title: str,
        album_description: str | None,
        album_picture_url: str | None,
        album_type: Literal['album', 'single'],
        album_created_at: date,
        album_updated_at: datetime,
        album_viewers_ids: list[int],
        album_likers_ids: list[int],
        album_artists_ids: list[int],
        album_tracks_ids: list[int],
        album_tags: list[str],
        dao_impl_factory: Callable[[], PostgresDAOImplementation],
        album: dict,
    ) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.create_album(
                title=album_title,
                album_type=album_type,
                created_at=album_created_at,
                updated_at=album_updated_at,
                viewers_ids=album_viewers_ids,
                likers_ids=album_likers_ids,
                artists_ids=album_artists_ids,
                tracks_ids=album_tracks_ids,
                tags=album_tags,
                picture_url=album_picture_url,
                description=album_description,
            )
        assert isinstance(response, int)
        assert response >= 1
        album['id'] = response

    async def test_get_album_by_id(
        self,
        album: dict,
        dao_impl_factory: Callable[[], PostgresDAOImplementation],
    ) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.get_album_by_id(album_id=album['id'])
        assert isinstance(response, Album | None)

    async def test_get_album_existance_by_title(
        self,
        artist_id: int,
        album_title: str,
        dao_impl_factory: Callable[[], PostgresDAOImplementation],
    ) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.get_album_existance_by_title(artist_id=artist_id, title=album_title)
        assert isinstance(response, bool)

    async def test_get_album_existance_by_id(self, album: dict, dao_impl_factory: Callable[[], PostgresDAOImplementation]) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.get_album_existance_by_id(album_id=album['id'])
        assert isinstance(response, bool)

    async def test_get_popular_albums(self, start: int, size: int, dao_impl_factory: Callable[[], PostgresDAOImplementation]) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.get_popular_albums(start=start, size=size)
        assert isinstance(response, list)

    async def test_count_artist_albums(self, artist_id: int, dao_impl_factory: Callable[[], PostgresDAOImplementation]) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.count_artist_albums(artist_id=artist_id)
        assert isinstance(response, int)
        assert response >= 0

    async def test_count_albums(self, dao_impl_factory: Callable[[], PostgresDAOImplementation]) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.count_albums()
        assert isinstance(response, int)
        assert response >= 0

    async def test_get_artist_id_by_user_id(self, user_id: int, dao_impl_factory: Callable[[], PostgresDAOImplementation]) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.get_artist_id_by_user_id(user_id=user_id)
        assert isinstance(response, int)
        assert response >= 1

    async def test_get_artist_existance_by_id(self, artist_id: int, dao_impl_factory: Callable[[], PostgresDAOImplementation]) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.get_artist_existance_by_id(artist_id=artist_id)
        assert isinstance(response, bool)

    async def test_get_artist_albums(self, artist_id: int, dao_impl_factory: Callable[[], PostgresDAOImplementation]) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.get_artist_albums(artist_id=artist_id)
        assert isinstance(response, list)

    async def test_update_album(
        self,
        album: dict,
        dao_impl_factory: Callable[[], PostgresDAOImplementation],
        album_title: str | None,
        album_picture_url: str | None,
        album_description: str | None,
        album_type: Literal['album', 'single'] | None,
        album_created_at: date | None,
        album_updated_at: datetime | None,
        album_viewers_ids: list[int] | None,
        album_likers_ids: list[int] | None,
        album_artists_ids: list[int] | None,
        album_tracks_ids: list[int] | None,
        album_tags: list[str] | None,
    ) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.update_album(
                album_id=album['id'],
                title=album_title,
                picture_url=album_picture_url,
                description=album_description,
                album_type=album_type,
                created_at=album_created_at,
                updated_at=album_updated_at,
                viewers_ids=album_viewers_ids,
                likers_ids=album_likers_ids,
                artists_ids=album_artists_ids,
                tracks_ids=album_tracks_ids,
                tags=album_tags,
            )
        assert isinstance(response, int)
        assert response >= 1
        album['id'] = response

    async def test_delete_album(self, album: dict, dao_impl_factory: Callable[[], PostgresDAOImplementation]) -> None:
        async with dao_impl_factory() as dao_impl:
            response = await dao_impl.delete_album(album_id=album['id'])  # type: ignore[func-returns-value]
        assert response is None


@pytest.fixture(scope='module')
def shared_data() -> dict:
    return {}


def test_one(shared_data: dict) -> None:
    shared_data['key'] = 'value'
    assert 'key' in shared_data


def test_two(shared_data: dict) -> None:
    assert shared_data['key'] == 'value'
