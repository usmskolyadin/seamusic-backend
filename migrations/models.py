from src.app.auth.artists.models import ArtistProfile, artist_to_tags_association, user_to_artist_association, \
    artist_to_track_association  # noqa: F401
from src.app.auth.producers.models import user_to_producer_association, producer_to_tags_association, \
    producer_to_soundkits_association, producer_to_beatpacks_association, ProducerProfile  # noqa: F401
from src.app.auth.users.models import User, user_to_tag_association, user_to_albums_association, \
    user_to_producer_association, user_to_artist_association, user_to_licenses_association, \
    user_to_playlists_association  # noqa: F401
from src.app.music.albums.interfaces.da.models import Album, album_to_artist_association, album_to_tag_association, \
    album_to_track_association  # noqa: F401
from src.app.music.beatpacks.models import Beatpack, beatpack_to_tag_association, beatpack_to_beat_association_table, \
    producer_to_beatpacks_association  # noqa: F401
from src.app.music.beats.models import Beat, tag_to_beat_association, producer_to_beat_association  # noqa: F401
from src.app.music.soundkits.models import Soundkit, tag_to_soundkits_association, beat_to_soundkits_association, \
    producer_to_soundkits_association  # noqa: F401
from src.app.music.squads.models import Squad, artist_to_squad_association, follower_to_squads_association, \
    producer_to_squad_association  # noqa: F401
from src.app.music.tracks.models import Track, track_to_tag_association, track_to_producer_association, \
    user_to_tracks_likes  # noqa: F401
from src.app.social.chats.models import message_to_chat_association, user_to_chat_association  # noqa: F401
from src.app.social.comments.models import user_to_comments_association  # noqa: F401
from src.app.social.licenses.models import License, user_to_licenses_association  # noqa: F401
from src.app.social.messages.models import Message, user_to_message_association, \
    message_to_chat_association  # noqa: F401
from src.app.social.notifications.models import Notification  # noqa: F401
from src.app.social.playlists.models import Playlist, playlists_to_tag_association, playlists_to_track_association, \
    author_to_playlists_association, playlists_to_beat_association  # noqa: F401
from src.app.social.tags.models import Tag  # noqa: F401
