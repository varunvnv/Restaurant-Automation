# from django.test import Client, TestCase


# from django.contrib.auth.models import User
# from django.test.client import Client

# # store the password to login later
# password = 'mypassword' 

# my_admin = User.objects.create_superuser('myuser', 'myemail@test.com', password)

# c = Client()

# # You'll need to log him in before you can send requests through the client
# c.login(username=my_admin.username, password=password)



# class TestLoggedUser(TestCase):
#     def setUp(self):
#         self.client = Client()

#         self.user = User.objects.create_user('test_user', 'user@test.net', 'secret')
#         self.user.save()
#         self.client.login(username='test_user', password='secret')

#     def tearDown(self):
#         self.user.delete()

#     def test_logged_user_get_homepage(self):
#         response = self.client.get(reverse('/'), follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_logged_user_get_settings(self):
#         response = self.client.get(reverse('/settings/'), follow=True)
#         self.assertEqual(response.status_code, 200)