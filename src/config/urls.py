"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core.routers import urlpatterns as core_api_urls
from usermanager.router import urlpatterns as usermanager_api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(core_api_urls)),
    path("api/v1/", include(usermanager_api_urls)),
    path("api/vi/login/", TokenObtainPairView.as_view(), name="api-login"),
    path("api/vi/token/refresh/", TokenRefreshView.as_view(), name="api-refresh-token"),
]
