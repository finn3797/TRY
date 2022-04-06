from masonite.routes import Route
# from app.resources.UserResource import UserResource

ROUTES = [
    Route.group([
        Route.get("", "WelcomeController@api").name('index'),
        Route.get("/test", "WelcomeController@api").name('test'),
        Route.get("ver", "api/AdminController@ver").name('ver'),
        Route.post("me", "api/AdminController@me").name('me'),
        Route.get("menu/my", "api/AdminController@mymenu").name('menu.my'),

        
        Route.post("notifi", "api/AdminController@sendNotifi").name('notifi.send'),
        Route.get("notifi", "api/AdminController@getNotifi").name('notifi.my'),
        Route.post("upload", "api/AdminController@upload").name('upload'),
    ],
        middleware=['guard:jwt'],
        # 认证关键
        name="api."),
    Route.api('users', "api.UsersController"),
    # UserResource('/x/users').routes(),
]
