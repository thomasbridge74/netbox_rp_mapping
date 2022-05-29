from django.test import TestCase
from netbox_rp_mapping.models import StaticRP, RPGroupEntry
from ipam.models import IPAddress, Prefix


class ValidateModels(TestCase):
    def setUp(self):
        host_prefix = Prefix.objects.create(prefix="226.0.0.1/32")
        group_prefix = Prefix.objects.create(prefix="225.0.1.0/24")
        ip = IPAddress.objects.create(address="212.17.32.1/32")
        rp = StaticRP.objects.create(
            rp_address=ip, override=False, rp_acl_name="THOMAS-TEST"
        )
        RPGroupEntry.objects.create(
            group_name=rp, sequence_no=20, remark=False, mcast_group=host_prefix
        )
        RPGroupEntry.objects.create(
            group_name=rp,
            sequence_no=10,
            remark=True,
            comments="Hello this is a remark",
        )
        RPGroupEntry.objects.create(
            group_name=rp, sequence_no=30, remark=False, mcast_group=group_prefix
        )

    def test_model_string(self):
        remark = RPGroupEntry.objects.get(sequence_no=10)
        hostline = RPGroupEntry.objects.get(sequence_no=20)
        prefixline = RPGroupEntry.objects.get(sequence_no=30)
        self.assertEqual(str(remark), "10 remark Hello this is a remark")
        self.assertEqual(str(hostline), "20 permit host 226.0.0.1")
        self.assertEqual(str(prefixline), "30 permit 225.0.1.0/24")
