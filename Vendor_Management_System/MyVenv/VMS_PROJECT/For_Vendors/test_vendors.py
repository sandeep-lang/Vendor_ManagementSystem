from django.test import TestCase
from For_Vendors.models import Vendor_details
from rest_framework.test import APIClient

class TestVendorCreation(TestCase):
    def setUp(self):
        # Create a test client
        self.client = APIClient()

    def test_create_vendor_valid_data(self):
        # Valid vendor data
        vendor_data = {
            "name": "Raja",
            "contact_details": "987654123",
            "address": "Hyderabad",
            "vendor_code": "A104"
        }

        response = self.client.post('/api/vendors/', vendor_data, format='json')

        # Check if the creation was successful (HTTP 201)
        self.assertEqual(response.status_code, 201)
        # Check if the response contains data
        self.assertTrue(response.data)  # Assuming the response should not be empty

    # Other test cases...
