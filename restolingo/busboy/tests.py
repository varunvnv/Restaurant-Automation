from django.test import TestCase
from placeorder.models import *
from django.contrib.auth.models import User


# Create your tests here.

class BusboyTests(TestCase):
    """
    Creates a new Table that is dirty
    status='dirty'
    Then test if we are correctly changing the status to available


    """


    def setUp(self):

        user_test = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user_test.save()
        dirty = Table(user_id=user_test, status='dirty')
        dirty.save()

    def test_dirty_is_made_available(self):
        table = Table.objects.get(id=1)
        table.status = 'available'
        self.assertEqual(table.status, 'available')



