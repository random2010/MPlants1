"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework import routers

from databook import views, api_views

router = routers.SimpleRouter()

router.register(r'users', api_views.DateModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.AddInfoFormView.as_view(),name='add'),
    path('delete/<int:pk>',views.DeleteInfoView.as_view(),name='delete'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/day-cbv/', api_views.DateListAPIView.as_view(), name='api/day-cbv/'),
    path('api/day-cbv-detail/<int:pk>', api_views.DateDetailAPIView.as_view(), name='api/day-cbv-detail/'),
    path('api/day-cbv-update/<int:pk>', api_views.DateUpdateAPIView.as_view(), name='api/day-cbv-update/'),
    path('',views.HomePageView.as_view(),name='home'),

] + router.urls
