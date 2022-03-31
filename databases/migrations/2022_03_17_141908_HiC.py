"""HiC Migration."""

from masoniteorm.migrations import Migration


class HiC(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("hi_cs") as table:
            table.increments("id")
            table.unsigned_integer("snp_id")
            table.string("rsid").nullable()
            table.string("chr_1").nullable()
            table.string("start_1").nullable()
            table.string("end_1").nullable()
            table.string("chr_2").nullable()
            table.string("start_2").nullable()
            table.string("end_2").nullable()
            table.string("score").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("hi_cs")
