from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class SignupView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
