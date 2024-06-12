from django.http import HttpResponseRedirect
from django.utils.decorators import decorator_from_fn

on_pause_redirect = decorator_from_fn(
    lambda func: lambda self, request, *args, **kwargs: (
        HttpResponseRedirect('pages:settings') if getattr(self.request.user, 'on_pause') else func(self, request, *args, **kwargs)
    )
)