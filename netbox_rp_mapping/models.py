from django.db import models
from netbox.models import NetBoxModel
from ipam.models import IPAddress, Prefix
from dcim.models import Site, Region
from django.urls import reverse

ACL_CHOICES = (("permit", "permit"), ("deny", "deny"), ("remark", "remark"))


class StaticRP(NetBoxModel):
    rp_address = models.ForeignKey(
        to=IPAddress, on_delete=models.DO_NOTHING, related_name="ip_address"
    )
    rp_acl_name = models.CharField(max_length=64, blank=False, unique=True)
    override = models.BooleanField(default=True)
    site = models.ForeignKey(to=Site, on_delete=models.DO_NOTHING, null=True)
    region = models.ForeignKey(to=Region, on_delete=models.DO_NOTHING, null=True)
    acl_counters = models.BooleanField(default=False)

    class Meta:
        ordering = ("rp_address",)
        verbose_name_plural = "Static RPs"

    def __str__(self):
        return str(self.rp_address)

    def get_absolute_url(self):
        return reverse("plugins:netbox_rp_mapping:staticrp", args=[self.pk])


class RPGroupEntry(NetBoxModel):
    group_name = models.ForeignKey(
        to=StaticRP, on_delete=models.CASCADE, related_name="mcast_rp"
    )
    sequence_no = models.PositiveBigIntegerField()
    acl_command = models.CharField(max_length=9, choices=ACL_CHOICES, default="remark")
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
        if self.acl_command == "remark":
            return f"{self.sequence_no} remark {self.comments}"
        if "/32" in str(self.mcast_group):
            host = str(self.mcast_group).replace("/32", "")
            end = f"host {host}"
        else:
            end = str(self.mcast_group)
        if self.acl_command == "deny":
            return f"{self.sequence_no} deny {end}"
        else:
            return f"{self.sequence_no} permit {end}"

    def get_absolute_url(self):
        return reverse("plugins:netbox_rp_mapping:rpgroupentry", args=[self.pk])
