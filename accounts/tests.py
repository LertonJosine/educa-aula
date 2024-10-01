from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import resolve, reverse
from .forms import CustomUserCreationForm
from .views import SignupView

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


class SignupTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    
    def test_signup_url(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
    
    def test_signup_view(self):
        view = resolve(reverse('signup'))
        self.assertEqual(view.func.__name__, SignupView.as_view().__name__)
    
    def test_signup_template(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        
    