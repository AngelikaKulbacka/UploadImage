from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Image


class ImageTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        self.image_data = {
            'name': 'Test Image',
            'image_file': 'test.jpg',
            'description': 'This is a test image',
            'user': self.user
        }
        self.response = self.client.post(
            reverse('image-list'),
            self.image_data,
            format='multipart'
        )

    def test_create_image(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(Image.objects.get().name, 'Test Image')

    def test_get_image_list(self):
        response = self.client.get(reverse('image-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Image')

    def test_get_image_detail(self):
        image = Image.objects.get()
        response = self.client.get(reverse('image-detail', args=[image.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Image')

    def test_update_image(self):
        image = Image.objects.get()
        new_data = {
            'name': 'Updated Image',
            'description': 'This image has been updated'
        }
        response = self.client.put(
            reverse('image-detail', args=[image.id]),
            new_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Image.objects.get().name, 'Updated Image')
        self.assertEqual(Image.objects.get().description, 'This image has been updated')

    def test_delete_image(self):
        image = Image.objects.get()
        response = self.client.delete(reverse('image-detail', args=[image.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Image.objects.count(), 0)
