from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import MyUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ["username", "email"]

UserAdmin.fieldsets = (
    (None, {
        "fields": (
            'notes',
        ),
    }),
)

admin.site.register(MyUser, UserAdmin)