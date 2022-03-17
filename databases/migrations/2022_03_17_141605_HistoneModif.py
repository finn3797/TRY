"""HistoneModif Migration."""

from masoniteorm.migrations import Migration


class HistoneModif(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("histone_modifs") as table:
            table.increments("id")
            table.unsigned_integer("snp_id")
            table.string("chr")
            table.string("chrom_start")
            table.string("chrom_end")
            table.string("signal")
            table.string("logp")
            table.string("profile_source")
            table.string("cell_line")
            table.string("cell_type")
            table.string("mark_type")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("histone_modifs")
