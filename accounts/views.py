from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy


class SignupView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'


class ProfileView(UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'registration/profile.html'
    