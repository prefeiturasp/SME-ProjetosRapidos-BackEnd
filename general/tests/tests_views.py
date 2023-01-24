import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from general.tests.tests_models import SetupData
from general.models import ContactMessage


class SellerViewSetTestCase(TestCase):

    entity = ContactMessage
    base_route = '/api/contact_message'

    def setUp(self):
        self.start = SetupData()
        self.client = APIClient()
        self.start.create_instance()

    def test_post(self):
        payload = {
            'name': 'José Matias',
            'email': 'josematias@gmail.com',
            'phone': '85986203456',
            'message': 'Lorem ipsum'
        }

        response = self.client.post(
            self.base_route + '/', data=payload, follow=True, format="json")

        self.assertTrue(status.is_success(response.status_code))
        self.assertTrue("id" in response.json())
