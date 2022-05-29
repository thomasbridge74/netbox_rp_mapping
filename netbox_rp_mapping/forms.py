from netbox.forms import NetBoxModelForm
from .models import StaticRP, RPGroupEntry
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from ipam.models import Prefix


class RPForm(NetBoxModelForm):
    class Meta:
        model = StaticRP
        fields = ("rp_address", "rp_acl_name", "override")


class RPGroupForm(NetBoxModelForm):
    comments = CommentField()
    mcast_group = DynamicModelChoiceField(queryset=Prefix.objects.all())

    class Meta:
        model = RPGroupEntry
        fields = (
            "group_name",
            "sequence_no",
            "remark",
            "mcast_group",
            "comments",
        )
