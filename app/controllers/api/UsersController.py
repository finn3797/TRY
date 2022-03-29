from masonite.controllers import Controller
from masonite.views import View
from app.models.User import User
from masonite.authentication import Auth


class UsersController(Controller):
    def index(self, view: View):
        return User.get()

    def show(self, view: View):
        return view.render("")

    def store(self, view: View):
        return view.render("")

    def update(self, view: View):
        return view.render("")

    def destroy(self, view: View):
        return view.render("")
