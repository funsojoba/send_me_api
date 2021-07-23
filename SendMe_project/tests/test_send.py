import unittest

from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from api.models.user import User

class Test(unittest.TestCase):
    client = APIClient()
    url = reverse('send-money')

    

    def test_anonymous_user_cannot_send(self):
        payload = {
            "amount":5000
        }
        res = self.client.post(self.url, payload)
        self.assertEqual(res.status_code, 401)
    
    def test_loggedin_user_can_send_money(self):
        User.objects.create_user(
        first_name="john",
        last_name="doe",
        email="testname@gmail.com", password='123456'
    )
        user = User.objects.get(email='testname@gmail.com')

        # self.client.force_authenticate(user=user)
        # payload = {
        #     "amount":5000
        # }
        # res = self.client.put(self.url, payload)
        # self.assertEqual(res.status_code, 200)
        print(user)

