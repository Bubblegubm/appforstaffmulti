from django.urls import path, include
from . import views


urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='registration'),
    path('edit/', views.edit, name='edit'),
    path('get_csrf/', views.get_csrf, name='get_csrf'),
]
