from django.test import TestCase
from django.db.utils import IntegrityError
from .models import User

# Create your tests here.
class UserRegistrationTest(TestCase):
    def test_register_no_data(self):
        user = User.objects.create(name='', email='testing@gmail.com', password='')
        