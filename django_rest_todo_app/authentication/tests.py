from django.urls import reverse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from user.models import User


class AuthViewsTests(APITestCase):

    def setUp(self):
        self.authentication_url = reverse('auth-login-list')
        self.registration_url = reverse('auth-registration-list')
        self.refresh_url = reverse('auth-refresh-list')

        self.username = 'apitest_user'
        self.email = 'apitest.user@email.com'
        self.password = 'contrasegna'

        self.data = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }

    def test_authentication_unactive_user(self):
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        user.is_active = False
        user.save()

        response = self.client.post(self.authentication_url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_authentication_active_user(self):
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)

        response = self.client.post(self.authentication_url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)

        self.assertTrue('user' in response.data)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_refresh_token(self):
        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)

        auth_response = self.client.post(self.authentication_url, self.data, format='json')
        access_token = auth_response.data['access']
        refresh_token = auth_response.data['refresh']

        refresh_response = self.client.post(self.refresh_url, {'refresh': refresh_token}, format='json')
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(refresh_response.data['access'], access_token, 'Token has not been refresh.')

    def test_registration(self):
        response = self.client.post(self.registration_url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.content)

        user = User.objects.get(email=self.email)
        response_user = response.data['user']

        self.assertEqual(response_user['id'], user.id)
    
    def test_authentication_with_random_token(self):
        client = APIClient()

        client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'random-token')
        response = client.get('/api/users/current/', data={'format': 'json'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication(self):
        client = APIClient()

        user = User.objects.create_user(username=self.username, email=self.email, password=self.password)

        auth_response = self.client.post(self.authentication_url, self.data, format='json')
        access_token = auth_response.data['access']

        client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = client.get('/api/users/current/', data={'format': 'json'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
