from django.urls import reverse
from django.http import HttpResponseRedirect
from functools import wraps

def on_pause_redirect(func):
    @wraps(func)
    def wrapper(self, request, *args, **kwargs):
        if getattr(self.request.user, 'on_pause'):
            return HttpResponseRedirect(reverse('settings:settings'))
        return func(self, request, *args, **kwargs)
    return wrapper