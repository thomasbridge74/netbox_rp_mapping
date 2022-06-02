from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import StaticRPSerializer, RPGroupEntrySerializer


class StaticRPViewSet(NetBoxModelViewSet):
    queryset = models.StaticRP.objects.prefetch_related("tags")
    serializer_class = StaticRPSerializer


class RPGroupEntryViewSet(NetBoxModelViewSet):
    queryset = models.RPGroupEntry.objects.prefetch_related("tags")
    serializer_class = RPGroupEntrySerializer
