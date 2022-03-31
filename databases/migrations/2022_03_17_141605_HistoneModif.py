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
            table.string("chr").nullable()
            table.string("chrom_start").nullable()
            table.string("chrom_end").nullable()
            table.string("signal").nullable()
            table.string("logp").nullable()
            table.string("profile_source").nullable()
            table.string("cell_line").nullable()
            table.string("cell_type").nullable()
            table.string("mark_type").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("histone_modifs")
