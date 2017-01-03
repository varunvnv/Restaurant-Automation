from django.contrib.auth.models import AnonymousUser, User, Group
from django.test import TestCase, RequestFactory



from .views import home

class TestUserLogin(TestCase):
    """
    In this unitest we try login as waiters to waiter page. The user
    should manage to login without any problem. 
    
    """
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.group, created = Group.objects.get_or_create(name='waiter')
        self.group.user_set.add(self.user)
 
    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/placeorder/index')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = self.user
        request.user.group = self.group

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at '/placeorder/index'
        response = home(request)
        self.assertEqual(response.status_code, 200)



class TestNonAuthorizedLogin(TestCase):
    """
    In this test we try to login without the proper authorization.
    This unittest should return 404 Error in order to be successful.

    """
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@xatz.com', password='top_gun')

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/placeorder/index')


        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = my_view(request)
        # Use this syntax for class-based views.
        response = MyView.as_view()(request)
        self.assertEqual(response.status_code, 404)

