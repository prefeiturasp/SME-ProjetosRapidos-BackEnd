from datetime import datetime, timedelta
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from project_request.tests.tests_models import SetupData
from project_request.models import ProjectRequest


class ProjectRequestViewSetTestCase(TestCase):

    entity = ProjectRequest
    base_route = '/api/project_request'

    def setUp(self):
        self.start = SetupData()
        self.client = APIClient()
        self.start.create_instance()

    def test_post(self):
        payload = {
            "name": "José Carlos",
            "contact": "josecarlos@gmail.com",
            "responsible_name": "José Carlos",
            "coordenadoria": "COTIC",
            "demand": "Projeto dia das crianças",
            "demand_type": "Uma demanda pontual (inscrições, divulgação de eventos, entre outros)",
            "approx_release_date": datetime.now() + timedelta(days=30),
            "target_users": "Pais das crianças",
            "approx_quantity_users": 500,
            "users_actions": "Realizar um cadastro",
            "external_factors": "Nenhum",
            "functionalities": "Página Inicial, Formulário de cadastro",
        }

        response = self.client.post(
            self.base_route + '/', data=payload, follow=True, format="json")

        self.assertTrue(status.is_success(response.status_code))
        self.assertTrue("id" in response.json())
