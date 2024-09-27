from django.test import TestCase
from django.contrib.auth import get_user_model

class AccountsTest(TestCase):
    
    def test_user_creation(self):
        user = get_user_model().objects.create_user('lerton', 'lerton@gmail.com', 'lerton123')
        self.assertEqual(user.username, 'lerton')
        self.assertTrue(user.is_active)
        self.assertEqual(user.email, 'lerton@gmail.com')
        self.assertFalse(user.is_superuser)
    
    
    def test_superuser_creation(self):
        super_user = get_user_model().objects.create_superuser('jozine', 'jozine@gmail.com', 'jozine123')
        self.assertTrue(super_user.is_active)
        self.assertEqual(super_user.username, 'jozine')
        self.assertEqual(super_user.email, 'jozine@gmail.com')
        self.assertTrue(super_user.is_superuser)

