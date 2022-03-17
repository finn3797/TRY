"""Species Migration."""

from masoniteorm.migrations import Migration


class Species(Migration):
    def up(self):
        """
        Run the migrations.
        """
        # 物种
        with self.schema.create("species") as table:
            table.increments("id")
            table.string("name")
            table.string("cover")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("species")
