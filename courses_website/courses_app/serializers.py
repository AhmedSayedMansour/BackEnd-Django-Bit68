from rest_framework import serializers
from courses_app import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password' : {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return user


class CourseSerializer(serializers.ModelSerializer):
    """Serializers courses"""

    class Meta:
        model = models.Course
        fields = ('id', 'name','category_id','details','price','created_at','updated_at','language')


class CategorySerializer(serializers.ModelSerializer):
    """Serializers categories"""

    class Meta:
        model = models.Category
        fields = ('id', 'name')


class ArticleSerializer(serializers.ModelSerializer):
    """Serializers articles"""

    class Meta:
        model = models.Category
        fields = ('id', 'title', 'body')


class PatenerSerializer(serializers.ModelSerializer):
    """Serializers parteners"""

    class Meta:
        model = models.Category
        fields = ('id', 'name', 'logo')