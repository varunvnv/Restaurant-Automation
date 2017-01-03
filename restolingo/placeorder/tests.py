from django.test import TestCase

# Create your tests here.

from .models import *

class EmployeeTests(TestCase):

    """
    Creates a new Employee for the restaurant, which means that this class
    creates a new username, password and a new role for the employee. The 
    role is defined using an integer.
    1 = manager, 2 = chef, 3 = host, 4 = waiter, 5 = busboy

    """

    def setUp(self):

        a_chef = Employee(username='maverick',password='topgun',role=2)
        a_chef.save()
        a_host  = Employee(username='boeing',password='747',role=3)
        a_host.save()
        a_waiter = Employee(username='atr',password='42',role=4)
        a_waiter.save()
        a_busboy = Employee(username='learjet',password='60',role=5)
        a_busboy.save()

    def test_new_employee_is_created_with_correct_role(self):
        
        chef = Employee.objects.get(username='maverick')
        self.assertEqual(chef.role, 2)

        host = Employee.objects.get(username='boeing')
        self.assertEqual(host.role, 3)

        waiter = Employee.objects.get(username='atr')
        self.assertEqual(waiter.role, 4)

        busboy = Employee.objects.get(username='learjet')
        self.assertEqual(busboy.role, 5)

#############################################################################


class TableTests(TestCase):

    """
    This unitest is supposed to check for correct assignment of a table 
    to the employee

    """

    def SetUp():

        a_waiter = Employee(username='atr',password='42',role=4)
        a_waiter.save()
        a_table = Table('what are the atributes')



    def test_if_table_is_assigned_to_the_waiter():

        waiter = Employee.objects.get(name='atr')
        table = Table.objects.get('which table')
        self.assertEqual()


##############################################################################












