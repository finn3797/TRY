"""Character Migration."""

from masoniteorm.migrations import Migration


class Character(Migration):
    def up(self):
        """
        Run the migrations.
        """
        # 性状
        with self.schema.create("characters") as table:
            table.increments("id")
            table.unsigned_integer("species_id")
            table.string("name")
            table.string("cover").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("characters")
