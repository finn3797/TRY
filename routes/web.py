from masonite.routes import Route
# from masonite.authentication import Auth
# from app.resources.UserResource import UserResource
from masonite.api import Api

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    # UserResource('/x/users').routes(),
    # Route.get('/api', 'WelcomeController@api')
]

# ROUTES += Auth.routes()

ROUTES += Api.routes(auth_route="/api/auth", reauth_route="/api/reauth")
