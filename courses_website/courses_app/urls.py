from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses_app import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('course', views.CourseViewSet)
router.register('category', views.CategoryViewSet)
router.register('article', views.ArticleViewSet)
router.register('partener', views.PartnerViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]