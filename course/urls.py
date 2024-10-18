from django.urls import path
from .views import ListCoursesPageView, CourseDetailsPageView

urlpatterns = [
    path('all/', ListCoursesPageView.as_view(), name='list_courses'),
    path('course_details/<int:pk>/', CourseDetailsPageView.as_view(), name='course_details'),
]
