"""
URL configuration for pereval project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from perevalapi.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'submitData', PerevalAddedViewSet)
router.register(r'users', UsersViewSet)
router.register(r'coords', CoordViewSet)
router.register(r'images', ImagesViewSet)
router.register(r'levels', LevelsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/perevaladded/', PerevalAddedListAPIView.as_view()),
    path('api/perevaladdeddetail/<int:pk>', PerevalAddedDetailAPIView.as_view()),
    path('api/users/', UsersListAPIView.as_view()),
    path('api/usersdetail/<int:pk>', UserDetailAPIView.as_view()),
    path('api/images/', ImagesListAPIView.as_view()),
    path('api/imagesdetail/<int:pk>', ImagesDetailAPIView.as_view()),
    path('api/coords/', CoordsListAPIView.as_view()),
    path('api/coordsdetail/<int:pk>', CoordsDetailAPIView.as_view()),

]