import time

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class ParkingSystemTestCase(APITestCase):

    def setUp(self):
        self.park_url = reverse('park-car-list')
        self.park_info = reverse('park-info-list')
        self.unpark_url = None
        self.data = [{"vehicle.registration_no": "SG 1234 23"},
                     {"vehicle.registration_no": "SG 2222 12"},
                     {"vehicle.registration_no": "SG 0909 11"}]     # .env SLOT_SIZE=3
        return super().setUp()

    def test_park_vehicle(self):
        time.sleep(10)
        for _ in self.data:
            response = self.client.post(self.park_url, data=_)
            print(response.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unpark(self):
        time.sleep(10)
        for _ in self.data:
            # Park
            response = self.client.post(self.park_url, data=_)
            print(response.data)
            # Unpark
            url = reverse('park-car-detail', args=[response.data['slot_no']])
            print(url)
            response = self.client.delete(url)
            print(response.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_info(self):
        time.sleep(10)
        print(self.park_info)
        for _ in self.data:
            # Park
            self.client.post(self.park_url, data=_)
        response = self.client.get(self.park_info)
        self.assertEqual(len(response.data), len(self.data))

    def test_throttle(self):
        # Making 11 request in 10 sec
        for _ in self.data:
            response = self.client.post(self.park_url, data=_)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        time.sleep(10)  # Test Throttle Make 10 request in 10 seconds & make one more request which will return empty
        for _ in range(0, 10):
            response = self.client.get(self.park_info)
            self.assertEqual(len(response.data), len(self.data))
        response = self.client.get(self.park_info)
        self.assertEqual(response.status_code, 429)