from django.test.testcases import SimpleTestCase
from django.urls import resolve, reverse
from .views import HomePageView


class PagesTest(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
            
    def test_home_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_home_page_use_correct_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    
    def test_home_page_url_uses_correct_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
    
    
    