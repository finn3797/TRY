"""AlertUserFields Migration."""

from masoniteorm.migrations import Migration


class AlertUserFields(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.string("avatar").nullable().after("name")
            table.text("desc").nullable().after("name")
            pass

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            table.drop_column("avatar", "desc")
            pass
