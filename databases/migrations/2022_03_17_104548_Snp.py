"""Snp Migration."""

from masoniteorm.migrations import Migration


class Snp(Migration):
    def up(self):
        """
        Run the migrations.
        """
        # 主要数据
        with self.schema.create("snps") as table:
            table.increments("id")
            table.unsigned_integer("species_id")
            table.unsigned_integer("character_id")
            table.string("rsid")
            table.string("chr")
            table.string("pos")
            table.string("ref")
            table.string("gene_locus")
            table.string("p_value")
            table.string("tf_motif")
            table.string("top_lead_id")
            table.string("top_lead_p")
            table.string("top_lead_rsquare")
            table.text("mark")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("snps")
