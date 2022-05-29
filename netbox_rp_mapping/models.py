from django.db import models
from netbox.models import NetBoxModel
from ipam.models import IPAddress, Prefix
from django.urls import reverse


class StaticRP(NetBoxModel):
    rp_address = models.ForeignKey(
        to=IPAddress, on_delete=models.DO_NOTHING, related_name="ip_address"
    )
    rp_acl_name = models.CharField(max_length=64, blank=False, unique=True)
    override = models.BooleanField(default=True)

    class Meta:
        ordering = ("rp_address",)
        verbose_name_plural = "Static RPs"

    def __str__(self):
        return str(self.rp_address)

    def get_absolute_url(self):
        return reverse("plugins:netbox_rp_mapping:rp", args=[self.pk])


class RPGroupEntry(NetBoxModel):
    group_name = models.ForeignKey(
        to=StaticRP, on_delete=models.CASCADE, related_name="mcast_rp"
    )
    sequence_no = models.PositiveBigIntegerField()
    remark = models.BooleanField()
    comments = models.CharField(max_length=128)
    mcast_group = models.ForeignKey(
        to=Prefix, on_delete=models.DO_NOTHING, related_name="mcast_groups", null=True
    )

    class Meta:
        ordering = (
            "group_name",
            "sequence_no",
        )
        verbose_name_plural = "RP Group Entries"

    def __str__(self):
        if self.remark:
            return f"{self.sequence_no} remark {self.comments}"
        elif "/32" in str(self.mcast_group):
            host = str(self.mcast_group).replace("/32", "")
            return f"{self.sequence_no} permit host {host}"
        else:
            return f"{self.sequence_no} permit {str(self.mcast_group)}"

    def get_absolute_url(self):
        return reverse("plugins:netbox_rp_mapping:rpgroup", args=[self.pk])
