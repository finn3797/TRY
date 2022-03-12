from masonite.routes import Route
# from app.resources.UserResource import UserResource

ROUTES = [
    Route.group([
        Route.get("", "WelcomeController@api").name('index'),
        Route.get("/test", "WelcomeController@api").name('test'),
    ],
        middleware=[],
        name="api."),
    Route.api('users', "api.UsersController"),
    # UserResource('/x/users').routes(),
]
