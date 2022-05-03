"""VetClinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from web_site.views import (
    IndexTemplate,
    AboutTemplate,
    DoctorsTemplate,
    DoctorTemplate,
    ServicesTemplate,
    ContactsTemplate,
)
from personal_area.views import user_login
from VetClinic import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplate.as_view(), name='index'),
    path('about/', AboutTemplate.as_view(), name='about'),
    path('doctors/', DoctorsTemplate.as_view(), name='doctors'),
    path('doctors/<int:pk>/', DoctorTemplate.as_view(), name='doctors-detail'),
    path('services/', ServicesTemplate.as_view(), name='services'),
    path('contacts/', ContactsTemplate.as_view(), name='contacts'),
    path('login/', user_login, name='login')
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

