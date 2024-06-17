from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from users.utils import on_pause_redirect

def index(request):
    template_name = 'pages/homepage.html'
    return render(request, template_name)

class PlaceholderView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/placeholder.html'

    @on_pause_redirect
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
