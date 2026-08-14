from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import override_settings


@override_settings(ALLOWED_HOSTS=['testserver', '127.0.0.1', 'localhost'])
class AuthFlowTests(TestCase):
    def test_user_can_register(self):
        client = Client()
        response = client.post(
            reverse('register'),
            {
                'username': 'alice123',
                'first_name': 'Alice',
                'last_name': 'Smith',
                'email': 'alice@example.com',
                'date_of_birth': '2000-01-01',
                'phone': '1234567890',
                'address': 'Test Street 1',
                'password1': 'StrongPass123!',
                'password2': 'StrongPass123!',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(get_user_model().objects.filter(username='alice123').exists())

    def test_user_can_login(self):
        user = get_user_model().objects.create_user(
            username='bob123',
            email='bob@example.com',
            password='StrongPass123!'
        )

        client = Client()
        response = client.post(
            reverse('login'),
            {'username': 'bob123', 'password': 'StrongPass123!'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertEqual(user.username, response.wsgi_request.user.username)
