from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import StaticRP, RPGroupEntry, ACL_CHOICES
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from ipam.models import Prefix, IPAddress
from dcim.models import Region, Site
from django import forms


class RPForm(NetBoxModelForm):
    region = DynamicModelChoiceField(queryset=Region.objects.all(), required=False)
    site = DynamicModelChoiceField(queryset=Site.objects.all(), required=False)

    class Meta:
        model = StaticRP
        fields = (
            "rp_address",
            "rp_acl_name",
            "override",
            "region",
            "site",
            "acl_counters",
        )


class RPGroupForm(NetBoxModelForm):
    comments = CommentField()
    mcast_group = DynamicModelChoiceField(
        queryset=Prefix.objects.filter(prefix__gt="224.0.0.0/4"),
        null_option="Select this if entering a remark",
    )

    class Meta:
        model = RPGroupEntry
        fields = (
            "group_name",
            "sequence_no",
            "acl_command",
            "mcast_group",
            "comments",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["mcast_group"].required = False


class StaticRPFilterForm(NetBoxModelFilterSetForm):
    model = StaticRP
    rp_address = forms.ModelChoiceField(
        queryset=IPAddress.objects.all(), required=False
    )
    rp_acl_name = forms.CharField(required=False)
    context = forms.BooleanField(required=False)


class RPGroupEntryFilterForm(NetBoxModelFilterSetForm):
    model = RPGroupEntry
    group_name = forms.ModelChoiceField(queryset=StaticRP.objects.all(), required=False)
    sequence_no = forms.IntegerField(required=False)
    acl_command = forms.ChoiceField(choices=ACL_CHOICES)
    mcast_group = forms.ModelChoiceField(queryset=Prefix.objects.all(), required=False)
    # comments = forms.Textarea(required=False)
