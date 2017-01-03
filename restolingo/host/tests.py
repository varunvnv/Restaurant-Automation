from django.test import TestCase
from placeorder.models import *

# Create your tests here.

class HostTests(TestCase):
    """
    Creates a new Table that is available
    status='available'
    Then test if we are correctly changing the status to occupied

      Creates a new Table that is occupied
    status='occupied'
    Then test if we are correctly changing the status to available
    """


    def setUp(self):
        user_test = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user_test.save()
        available = Table(user_id = user_test, status = 'available')
        available.save()
        occupied = Table(user_id=user_test, status='occupied')
        occupied.save()

    def test_available_is_made_occupied(self):
        table = Table.objects.get(id=1)
        table.status = 'occupied'
        self.assertEqual(table.status, 'occupied')

    def test_occupied_is_made_available(self):
        table = Table.objects.get(id=2)
        table.status = 'available'
        self.assertEqual(table.status, 'available')


