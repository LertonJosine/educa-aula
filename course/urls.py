from django.urls import path
from .views import ListCoursesPageView

urlpatterns = [
    path('all/', ListCoursesPageView.as_view(), name='list_courses'),
]
