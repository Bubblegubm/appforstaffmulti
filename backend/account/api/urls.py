from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'account'

router = routers.DefaultRouter()
router.register(r'organization', views.OrganizationView)
router.register(r'profile', views.ProfileView)

urlpatterns = [
    path('', include(router.urls))
]
