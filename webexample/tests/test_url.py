

from django.test import TestCase, Client, override_settings

from rest_framework import status


#@override_settings(API_KEY='0')
from djangoProject import settings


class HeaderTest(TestCase):
    client = Client()

    def test_get_bad_header(self):
        response = self.client.get('/pets', X_API_KEY='2')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_bad_header(self):
        response = self.client.post('/pets', HTTP_X_API_KEY='2')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_bad_header(self):
        response = self.client.delete('/pets/1', X_API_KEY='2')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_photo_bad_header(self):
        response = self.client.post('/pets/1/photo', X_API_KEY='2')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_get_good_header(self):
        response = self.client.get('/pets', HTTP_X_API_KEY=settings.API_KEY)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_good_header(self):
        """Возвращает 400"""
        response = self.client.post('/pets', HTTP_X_API_KEY=settings.API_KEY)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_good_header(self):
        """Возвращает 404, т.к. нет pet id 1 в БД"""
        response = self.client.delete('/pets/1', HTTP_X_API_KEY=settings.API_KEY)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_photo_good_header(self):
        response = self.client.post('/pets/1/photo', HTTP_X_API_KEY=settings.API_KEY)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
