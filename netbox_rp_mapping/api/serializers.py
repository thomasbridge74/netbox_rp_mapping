from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import RPGroupEntry, StaticRP
from ipam.api.serializers import NestedPrefixSerializer


class StaticRPSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_rp_mapping-api:staticrp-detail"
    )

    class Meta:
        model = StaticRP
        fields = (
            "id",
            "url",
            "display",
            "rp_address",
            "rp_acl_name",
            "override",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )


class RPGroupEntrySerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_rp_mapping-api:rpgroupentry-detail"
    )
    mcast_group = NestedPrefixSerializer()

    class Meta:
        model = RPGroupEntry
        fields = (
            "id",
            "url",
            "group_name",
            "sequence_no",
            "acl_command",
            "comments",
            "mcast_group",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
