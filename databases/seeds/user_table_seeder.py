"""UserTableSeeder Seeder."""
from masoniteorm.seeds import Seeder
from masonite.facades import Hash
import hashlib

from app.models.User import User


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.truncate()
        # u = User.where('email', 'admin@admin.com').force_delete()
        # print(u)
        # 因为前端加密密码 此处也处理
        # print(hashlib.md5(b'123456').hexdigest())
        User.create(
            {
                "name": "Osindex",
                "avatar": "/img/logo.png",
                "email": "admin@admin.com",
                "password": Hash.make(hashlib.md5(b'123456').hexdigest()),
                "phone": "+123456789",
            }
        )
