from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager fmor user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'#used in the login user_name
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    details = models.TextField()
    price = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    language = models.CharField(max_length=16)

    def __str__(self) -> str:
        return 'Course name : ' + self.name


class CourseImage(models.Model):
    image_path = models.FilePathField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_images")

    def __str__(self) -> str:
        return 'Course name : ' + self.course_id.name


class CourseVideo(models.Model):
    video_path = models.FilePathField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_videos")
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return 'Course name : ' + self.name


class Insturctor(models.Model):
    name = models.CharField(max_length=255)
    image = models.FilePathField()
    description = models.TextField()
    rate = models.FloatField()

    def __str__(self) -> str:
        return 'Insturctor name : ' + self.name


class CourseInstructor(models.Model):
    instructor_id = models.ForeignKey(Insturctor, on_delete=models.CASCADE, related_name="course_instructors")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'Insturctor name : ' + self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return 'Article tilte : ' + self.title

class Partener(models.Model):
    name = models.CharField(max_length=255)
    logo = models.FilePathField()

    def __str__(self) -> str:
        return 'Partner name : ' + self.name