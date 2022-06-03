from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets, models


class StaticRPType(NetBoxObjectType):
    class Meta:
        model = models.StaticRP
        fields = "__all__"


class RPGroupEntryType(NetBoxObjectType):
    class Meta:
        model = models.RPGroupEntry
        fields = "__all__"
        filterset_class = filtersets.RPGroupEntryFilterSet


class Query(ObjectType):
    staticrp = ObjectField(StaticRPType)
    staticrp_list = ObjectListField(StaticRPType)
    rpgroup_entry = ObjectField(RPGroupEntryType)
    rpgroup_entry_list = ObjectListField(RPGroupEntryType)


schema = Query
