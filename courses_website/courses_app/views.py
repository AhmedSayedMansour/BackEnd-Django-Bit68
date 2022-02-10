from django.shortcuts import render
from rest_framework import viewsets, status, filters
from profiles_api import serializers, models, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly    #not Auth but can read
from rest_framework.permissions import IsAuthenticated              #not Auth can't read


class PartnerViewSet(viewsets.ModelViewSet):
    """Handles reading Partners """
    serializer_class = serializers.PartnerSerializer
    queryset = models.Partner.objects.all()
    #authentication_classes = ---
    #permission_classes = ---
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')