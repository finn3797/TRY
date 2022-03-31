"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from masonite.api.authentication import AuthenticatesTokens
from masonite.notification import Notifiable


class User(Model, AuthenticatesTokens, SoftDeletesMixin, Authenticates, Notifiable):
    """User Model."""

    __fillable__ = ["name", "email", "password", "avatar", "phone"]
    __hidden__ = ["password"]
    __auth__ = "email"
