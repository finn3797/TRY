"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash

from app.models.User import User


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            {
                "name": "Osindex",
                "email": "admin@admin.com",
                "password": Hash.make("123456"),
                "phone": "+123456789",
            }
        )
