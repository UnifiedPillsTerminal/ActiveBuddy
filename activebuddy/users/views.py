from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'register/register_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')