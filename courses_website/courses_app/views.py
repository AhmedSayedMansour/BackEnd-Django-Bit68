from django.shortcuts import render
from rest_framework import viewsets, status, filters
from courses_app import serializers, models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly    #not Auth but can read
from rest_framework.permissions import IsAuthenticated              #not Auth can't read


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    #permission_classes = ---
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class CourseViewSet(viewsets.ModelViewSet):
    """Handles reading courses"""
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()
    #authentication_classes = ---
    #permission_classes = ---
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'category_id', 'price', 'updated_at', 'language',)


class CategoryViewSet(viewsets.ModelViewSet):
    """Handles reading categories"""
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    #authentication_classes = ---
    #permission_classes = ---
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class ArticleViewSet(viewsets.ModelViewSet):
    """Handles reading articles"""
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()
    #authentication_classes = ---
    #permission_classes = ---
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class PartnerViewSet(viewsets.ModelViewSet):
    """Handles reading Partners """
    serializer_class = serializers.PartnerSerializer
    queryset = models.Partner.objects.all()
    #authentication_classes = ---
    #permission_classes = ---
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
