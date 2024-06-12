from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

class SettingsListView(LoginRequiredMixin, ListView):
    model = get_user_model()
    template_name = 'pages/settings.html'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['email'] = user.email
        context['on_pause'] = user.on_pause
        context['backup_email'] = user.backup_email
        return context

    def post(self, request, *args, **kwargs):
        user = self.get_object()

        email = request.POST.get('email', '')
        on_pause = request.POST.get('on_pause', False) == 'True'
        backup_email = request.POST.get('backup_email', '')

        user.email = email
        user.on_pause = on_pause
        user.backup_email = backup_email
        user.save()

        return redirect('settings:settings')