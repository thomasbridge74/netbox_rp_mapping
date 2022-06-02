from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import StaticRP, RPGroupEntry
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from ipam.models import Prefix, IPAddress
from django import forms


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


class StaticRPFilterForm(NetBoxModelFilterSetForm):
    model = StaticRP
    rp_address = forms.ModelChoiceField(
        queryset=IPAddress.objects.all(), required=False
    )
    rp_acl_name = forms.CharField(required=False)
    context = forms.BooleanField(required=False)
