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
            table.string("chr")
            table.string("pos")
            table.string("anc")
            table.string("gc")
            table.string("cpg")
            table.string("score_seg_dup")
            table.string("pri_ph_cons")
            table.string("mam_ph_cons")
            table.string("ver_ph_cons")
            table.string("pri_phylop")
            table.string("mam_phylop")
            table.string("ver_phylop")
            table.string("gerp_n")
            table.string("gerp_s")
            table.string("b_statistic")
            table.string("fit_cons_all")
            table.string("si_phy")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("conservations")
