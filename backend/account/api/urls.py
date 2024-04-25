from django.urls import path, include
from rest_framework import routers
from . import views


app_name = 'account'

router = routers.DefaultRouter()
router.register(r'organization', views.OrganizationView)

urlpatterns = [
    path('organization/',
         views.OrganizationListView.as_view(),
         name='organization_list'),
    path('organization/<pk>/',
         views.OrganizationDetailView.as_view(),
         name='organization_detail'),
    path('profile/',
         views.UserListView.as_view(),
         name='user_list'),
    path('profile/<pk>/',
         views.UserDetailView.as_view(),
         name='user_detail'),
    path('', include(router.urls))
]
