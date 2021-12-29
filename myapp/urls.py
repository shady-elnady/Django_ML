"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
# from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views
from digit.api.views import DigitViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from digit.views import *

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'digit', DigitViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('image_upload/', digit_image_view, name = 'image_upload'),
    path('digit_images/', display_digit_images, name = 'digit_images'),
    path('canvas/', canvas_image, name = 'canvas'),
    path('api/', include(router.urls)),
    path('api/it/', csrf_exempt(views.ApiView.as_view())),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    # Put the API and admin routes about so they don't get eaten by the matcher?
    # must be catch-all for pushState to work
    path(r'^', views.FrontendAppView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)