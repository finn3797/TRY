"""Annotation Migration."""

from masoniteorm.migrations import Migration


class Annotation(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("annotations") as table:
            table.increments("id")
            table.unsigned_integer("snp_id")
            table.string("factor_id")
            table.string("genotype")
            table.string("strand")
            table.string("start")
            table.string("end")
            table.string("relative_position")
            table.string("binding_affinity_change")
            table.string("allele_orientation")
            table.string("variant_affinity_effect")
            table.string("effect_p_value")
            table.string("motif")
            table.timestamps()
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("annotations")
