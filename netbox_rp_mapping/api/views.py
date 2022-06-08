from netbox.api.viewsets import NetBoxModelViewSet

from netbox_rp_mapping import models, filtersets
from .serializers import StaticRPSerializer, RPGroupEntrySerializer


class StaticRPViewSet(NetBoxModelViewSet):
    queryset = models.StaticRP.objects.prefetch_related("tags")
    serializer_class = StaticRPSerializer
    filterset_class = filtersets.StaticRPFilterSet


class RPGroupEntryViewSet(NetBoxModelViewSet):
    queryset = models.RPGroupEntry.objects.prefetch_related("tags")
    serializer_class = RPGroupEntrySerializer
    filterset_class = filtersets.RPGroupEntryFilterSet
