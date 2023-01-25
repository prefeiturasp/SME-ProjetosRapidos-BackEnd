from datetime import datetime, timedelta
from django.test import TestCase
from project_request.models import ProjectRequest


class SetupData:
    def create_instance(self):
        obj = {
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
        ProjectRequest.objects.create(**obj)


class ProjectRequestTestCase(TestCase):
    start = SetupData()
    entity = ProjectRequest

    def setUp(self):
        self.start.create_instance()

    def test_get(self):
        instance = self.entity.objects.first()
        self.assertIsInstance(instance, self.entity)

    def test_update(self):
        instance = self.entity.objects.first()
        instance.name = "José Carlos"
        instance.save()
        self.assertEqual(instance.name, "José Carlos")

    def test_delete(self):
        instance = self.entity.objects.first()
        instance.delete()

        self.assertFalse(instance.id)
        self.assertIsInstance(instance, self.entity)
