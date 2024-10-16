from django.test.testcases import SimpleTestCase
from django.urls import resolve, reverse
from .views import HomePageView, AboutPageView, TrainersPageView


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
        

class AboutTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
    
    def test_about_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_about_page_template(self):
        self.assertContains(self.response, 'About')
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_about_page_view(self):
        view = resolve(reverse('about'))
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
    


class TrainersTests(SimpleTestCase):
    def setUp(self):
        url = reverse('trainers')
        self.response = self.client.get(url)
    
    
    def test_trainers_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_trainers_page_template(self):
        self.assertContains(self.response, 'Trainers')
        self.assertTemplateUsed(self.response, 'trainers.html')
    
    def test_trainers_page_view(self):
        view = resolve(reverse('trainers'))
        self.assertEqual(view.func.__name__, TrainersPageView.as_view().__name__)
    
    

    
    
    