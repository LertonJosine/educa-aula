from django.test import TestCase
from .models import Course
from .views import CourseDetailsPageView, ListCoursesPageView, CreateCourseView
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model


class CourseTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@gmail.com',
            password='test123'

        )
        self.course = Course.objects.create(
            trainer = self.user,
            name = 'test course',
            resume = 'This course is created for test purposes',
            sits = 10,
            price=200,
            cover = '../media/course-1.jpg'
        )
        
        url = reverse('list_courses')
        self.response = self.client.get(url)

    
    def test_course_creation(self):
        self.assertEqual(self.course.trainer, self.user)
        self.assertEqual(self.course.name, 'test course')
        self.assertEqual(self.course.resume, 'This course is created for test purposes')
        self.assertEqual(self.course.sits, 10)
        self.assertEqual(self.course.price, 200)
    
    def test_course_list_all_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_course_list_all_page_template(self):
        self.assertContains(self.response, 'Courses')
        self.assertTemplateUsed(self.response, 'list_courses.html')
    
    def test_course_list_all_page_view(self):
        view = resolve(reverse('list_courses'))
        self.assertEqual(view.func.__name__, ListCoursesPageView.as_view().__name__)


class CourseDetailsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@gmail.com',
            password='test123'

        )
        self.course = Course.objects.create(
            trainer = self.user,
            name = 'test course',
            resume = 'This course is created for test purposes',
            sits = 10,
            price=200,
            cover = '../media/course-1.jpg'
        )
        url = reverse('course_details', args=[self.course.pk])
        self.response = self.client.get(url)
    
    def test_course_details_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_course_details_template(self):
        self.assertContains(self.response, 'Course Details')
        self.assertTemplateUsed(self.response, 'course_details.html')
    
    def test_course_detauls_page_view(self):
        view = resolve(reverse('course_details', args=[self.course.pk]))
        self.assertEqual(view.func.__name__, CourseDetailsPageView.as_view().__name__)
    

class CoursePageTests(TestCase):
    def setUp(self):
        super_user = get_user_model().objects.create_superuser(
            username='test',
            email='test@gmail.com',
            password= 'test123'
            )
        self.client.login(username=super_user.username, email=super_user.email, password='test123')
        url = reverse('create_course')
        self.response = self.client.get(url)
    
    def test_create_course_page_name(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_course_create_page_template(self):
        self.assertContains(self.response, 'Create Course')
        self.assertTemplateUsed(self.response, 'create_course.html')
    
    def test_create_course_page_view(self):
        view = resolve('/courses/create_course/')
        self.assertEqual(view.func.__name__, CreateCourseView.as_view().__name__)
    
    def test_create_course_page_redirects_not_logged_users(self):
        self.client.logout()
        response = self.client.get(reverse('create_course'))
        self.assertRedirects(response, expected_url='/accounts/login/?next=/courses/create_course/')
    
    def test_create_course_page_only_super_user_can_access(self):
        user = get_user_model().objects.create_user(
            username='test2',
            email='test2@gmail.com',
            password='test123'
        )
        self.client.login(username=user.username, email=user.email, password='test123')
        response = self.client.get(reverse('create_course'))
        self.assertEqual(response.status_code, 403)
        
    
    