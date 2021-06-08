from django.test import TestCase
import json
from rest_framework import status
from django.test import Client
from django.urls import reverse
from rest_framework.test import APIClient

# Create your tests here.


class DistributeTestSuccess(TestCase):
    """ Test module for GET all data """

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.distribute_data = {'total_amount': 100, 'id1': 'user01', 'share1': '0.02'}
        self.response = self.client.get(
            reverse('distribute'),
            self.distribute_data,
            format="json")

    def test_distribute_api_success(self):
        """Test the api is succeed"""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


class DistributeTestWithNoData(TestCase):
    """ Test module for No data"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.distribute_data = {}
        self.response = self.client.get(
            reverse('distribute'),
            self.distribute_data,
            format="json")

    def test_distribute_api_success(self):
        """Test the api is succeed"""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


class DistributeTestWithUserMissing(TestCase):
    """ Test module for invalid data """

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.distribute_data = {'total_amount': 100}
        self.response = self.client.get(
            reverse('distribute'),
            self.distribute_data,
            format="json")

    def test_distribute_api_success(self):
        """Test the api is succeed"""
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

