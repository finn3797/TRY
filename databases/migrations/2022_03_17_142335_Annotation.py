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
            table.string("factor_id").nullable()
            table.string("genotype").nullable()
            table.string("strand").nullable()
            table.string("start").nullable()
            table.string("end").nullable()
            table.string("relative_position").nullable()
            table.string("binding_affinity_change").nullable()
            table.string("allele_orientation").nullable()
            table.string("variant_affinity_effect").nullable()
            table.string("effect_p_value").nullable()
            table.string("motif").nullable()
            table.timestamps()
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("annotations")
