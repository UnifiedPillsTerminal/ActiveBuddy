from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm
from .models import MyUser

class RegisterView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('pages:homepage')
