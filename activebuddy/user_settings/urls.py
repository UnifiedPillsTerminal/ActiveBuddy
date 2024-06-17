from django.urls import path

from . import views

app_name = 'settings'

urlpatterns = [
    path('', views.SettingsListView.as_view(), name='settings'),
]

    # path(
    #     "email/change/",
    #     views.BaseEmailChangeView.as_view(),
    #     name="base_email_update",
    # ),
    # path(
    #     "email/change/done",
    #     views.EmailChangeDoneView.as_view(),
    #     name="email_change_done",
    # )