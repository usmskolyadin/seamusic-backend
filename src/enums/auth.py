from enum import Enum


class Role(str, Enum):
    artist = "artist"
    producer = "producer"
    listener = "listener"


class AccessLevel(str, Enum):
    user = "user"
    admin = "admin"
    superuser = "superuser"


class PremiumLevel(str, Enum):
    none = "none"
    bot = "bot"
    full = "full"
