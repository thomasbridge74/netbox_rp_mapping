from netbox.filtersets import NetBoxModelFilterSet
from .models import StaticRP, RPGroupEntry


class StaticRPFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = StaticRP
        fields = ("id", "rp_address", "rp_acl_name", "override", "region", "site")

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class RPGroupEntryFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = RPGroupEntry
        fields = (
            "id",
            "group_name",
            "sequence_no",
            "acl_command",
            "mcast_group",
            "comments",
        )

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
