from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class ListCoursesPageView(ListView):
    model = Course
    template_name = 'list_courses.html'
    context_object_name = 'courses'


class CourseDetailsPageView(DetailView):
    model = Course
    template_name = 'course_details.html'
    context_object_name = 'course'


class CreateCourseView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Course
    template_name = 'create_course.html'
    fields = ['name', 'trainer', 'sits', 'price', 'cover', 'resume']
    permission_required = ('is_superuser',)
    
    
    