"""Conservation Migration."""

from masoniteorm.migrations import Migration


class Conservation(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("conservations") as table:
            table.increments("id")
            table.unsigned_integer("snp_id")
            table.string("chr").nullable()
            table.string("pos").nullable()
            table.string("anc").nullable()
            table.string("gc").nullable()
            table.string("cpg").nullable()
            table.string("score_seg_dup").nullable()
            table.string("pri_ph_cons").nullable()
            table.string("mam_ph_cons").nullable()
            table.string("ver_ph_cons").nullable()
            table.string("pri_phylop").nullable()
            table.string("mam_phylop").nullable()
            table.string("ver_phylop").nullable()
            table.string("gerp_n").nullable()
            table.string("gerp_s").nullable()
            table.string("b_statistic").nullable()
            table.string("fit_cons_all").nullable()
            table.string("si_phy").nullable()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("conservations")
