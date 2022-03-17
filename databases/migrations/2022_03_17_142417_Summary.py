"""Summary Migration."""

from masoniteorm.migrations import Migration


class Summary(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("summaries") as table:
            table.increments("id")
            table.unsigned_integer("snp_id")
            table.text("content")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("summaries")
