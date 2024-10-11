from django.urls import path
from .views import HomePageView, AboutPageView, TrainersPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('trainers/', TrainersPageView.as_view(), name='trainers'),
]
