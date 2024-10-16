from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import resolve, reverse
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .views import SignupView, ProfileView

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
        

class ProfileTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@gmail.com',
            password='test123'
        )
        self.user2 =get_user_model().objects.create_user(
            username='test2',
            email='test2@gmail.com',
            password='test123'
        )
        
        url = reverse('profile', args=[self.user.pk])
        self.client.login(username=self.user.username, password='test123')
        self.respose = self.client.get(url)
    
    def test_profile_name(self):
        self.assertEqual(self.respose.status_code, 200)
    
    def test_profile_page_template(self):
        self.assertContains(self.respose, 'Profile')
        self.assertTemplateUsed(self.respose, 'registration/profile.html')
    
    def test_profile_user_can_only_access_his_data(self):
        url = reverse('profile', args=[self.user2.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
    
    def test_profile_form_used(self):
        form = self.respose.context['form']
        self.assertIsInstance(form, CustomUserChangeForm)
    
    def test_profile_view_used(self):
        view = resolve(reverse('profile', args=[self.user.pk]))
        self.assertEqual(view.func.__name__, ProfileView.as_view().__name__)
    
    def test_profile_only_login_user(self):
        self.client.logout()
        response = self.client.get(reverse('profile', args=[self.user.pk]))
        self.assertRedirects(response, f"/accounts/login/?next=/accounts/profile/{self.user.pk}/")