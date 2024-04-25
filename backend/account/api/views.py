from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from account.models import Organization, Profile
from account.api.serializers import OrganizationSerializer, UserSerializer


class OrganizationListView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetailView(generics.RetrieveAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OrganizationView(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

