from masonite.routes import Route
# from app.resources.UserResource import UserResource

ROUTES = [
    Route.group([
        Route.get("", "WelcomeController@api").name('index'),
        Route.get("/test", "WelcomeController@api").name('test'),
        Route.post("me", "api/AdminController@me").name('me'),
        Route.get("menu/my", "api/AdminController@mymenu").name('menu.my'),
        Route.get("ver", "api/AdminController@ver").name('ver'),
    ],
        middleware=['guard:jwt'],
        # 认证关键
        name="api."),
    Route.api('users', "api.UsersController"),
    # UserResource('/x/users').routes(),
]
