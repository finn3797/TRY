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
            table.string("rsid").nullable()
            table.string("chr").nullable()
            table.string("pos").nullable()
            table.string("ref").nullable()
            table.string("gene_locus").nullable()
            table.string("p_value").nullable()
            table.string("tf_motif").nullable()
            table.string("top_lead_id").nullable()
            table.string("top_lead_p").nullable()
            table.string("top_lead_rsquare").nullable()
            table.text("mark").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("snps")
