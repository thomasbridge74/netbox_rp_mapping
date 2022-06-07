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
    mcast_group = DynamicModelChoiceField(
        queryset=Prefix.objects.all(), null_option="Select this if entering a remark"
    )

    class Meta:
        model = RPGroupEntry
        fields = (
            "group_name",
            "sequence_no",
            "remark",
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
    remark = forms.BooleanField(required=False)
    mcast_group = forms.ModelChoiceField(queryset=Prefix.objects.all(), required=False)
    # comments = forms.Textarea(required=False)
