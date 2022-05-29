from django.test import TestCase
from netbox_rp_mapping.models import StaticRP, IPAddress


class ValidateModels(TestCase):
    def test_model_name(self):
        self.assertEqual(1, 2)
