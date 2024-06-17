from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('ss/', views.PlaceholderView.as_view(), name='placeholder'),
]