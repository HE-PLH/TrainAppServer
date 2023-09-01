"""
URL configuration for Inquiries project.

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
from django.conf import settings
from django.conf.urls.static import static
from mpesa.urls import mpesa_urls


from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mpesa/', include(mpesa_urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path('api/(?P<version>(v1|v2))/', include('authentication.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('resource.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('booking.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('schedule.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('tutorials.urls')),
    # re_path('api/(?P<version>(v1|v2))/', include('mpesa.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

