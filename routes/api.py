from masonite.routes import Route

ROUTES = [
    Route.group([
        Route.get("/test", "WelcomeController@api").name('/test'),
    ],
        prefix="/api",
        middleware=['web', 'cors'],
        name="api."),
    # Route.api('users', "api.UserController")
]
