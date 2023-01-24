from django.test import TestCase
from general.models import ContactMessage


class SetupData:
    def create_instance(self):
        ContactMessage.objects.create(
            name='José Matias',
            email='josematias@gmail.com',
            phone='85986203456',
            message="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
        )


class ContactMessageTestCase(TestCase):
    start = SetupData()
    entity = ContactMessage

    def setUp(self):
        self.start.create_instance()

    def test_get(self):
        instance = self.entity.objects.first()
        self.assertIsInstance(instance, self.entity)

    def test_update(self):
        instance = self.entity.objects.first()
        instance.name = 'José Matias'
        instance.save()
        self.assertEqual(instance.name, 'José Matias')

    def test_delete(self):
        instance = self.entity.objects.first()
        instance.delete()

        self.assertFalse(instance.id)
        self.assertIsInstance(instance, self.entity)
