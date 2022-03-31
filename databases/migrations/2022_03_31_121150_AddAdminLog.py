"""AddAdminLog Migration."""

from masoniteorm.migrations import Migration


class AddAdminLog(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("add_admin_logs") as table:
            table.increments("id")
            table.unsigned_integer("user_id")
            table.string("operate")
            # 查询、编辑、新增、删除、操作
            table.string("mod").nullable()
            # 系统、用户、XX表
            table.string("describe")
            # 成功、修改xxxx
            table.timestamps()
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("add_admin_logs")
