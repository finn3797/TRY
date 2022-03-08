from masonite.routes import Route
from masonite.authentication import Auth
from masonite.api import Api

ROUTES = [
	Route.get("/", "WelcomeController@show"),
]

ROUTES += Auth.routes()
ROUTES += Api.routes(auth_route="/api/auth", reauth_route="/api/reauth")
