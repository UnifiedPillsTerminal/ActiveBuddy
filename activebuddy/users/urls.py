from django.urls import path
from django.contrib.auth import views as inbuilt

from . import views

app_name = 'users'

urlpatterns = [
    path('', inbuilt.LoginView.as_view(), name="login"),
    path('logout/', inbuilt.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('pwd-recovery/', inbuilt.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "pwd-recovery/done/",
        inbuilt.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("new-pwd/", inbuilt.PasswordResetView.as_view(), name="password_reset"),
    path(
        "new-pwd/email-sent/",
        inbuilt.PasswordResetDoneView.as_view(),
        name="password_email_sent",
    ),
    path(
        "new-pwd/<uidb64>/<token>/",
        inbuilt.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "new-pwd/done/",
        inbuilt.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
