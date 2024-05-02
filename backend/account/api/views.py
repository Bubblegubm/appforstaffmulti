from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from account.models import Organization, Profile
from account.api.serializers import OrganizationSerializer, ProfileSerializer


class OrganizationView(viewsets.ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ProfileView(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
