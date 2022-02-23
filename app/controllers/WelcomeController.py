"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from app.helpers import helper


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("welcome")

    def api(self):
    	return ["apple", "pear", 233]
