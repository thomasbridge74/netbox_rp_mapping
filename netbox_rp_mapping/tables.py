import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import StaticRP, RPGroupEntry


class RPTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = StaticRP
        fields = ("pk", "rp_address", "rp_acl_name", "override")
        default_columns = ("pk", "rp_address", "rp_acl_name", "override")

    rp_address = tables.Column(linkify=True)


class GroupTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        model = RPGroupEntry
        fields = (
            "pk",
            "group_name",
            "sequence_no",
            "acl_command",
            "mcast_group",
            "comments",
        )
        default_columns = (
            "pk",
            "group_name",
            "sequence_no",
            "acl_command",
            "mcast_group",
            "comments",
        )

    group_name = tables.Column(linkify=True)
    mcast_group = tables.Column(linkify=True)
