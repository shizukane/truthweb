"""awwardproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from re import template
from django.urls import re_path as url , include
from django.contrib import admin
from django.contrib.auth import views
from awardapp.forms import RegisterForm
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('awardapp.urls')),
    url(r'^accounts/register/$',RegistrationView.as_view(form_class=RegisterForm,template_name="django_registration/registration_form.html" ),{"next_page": '/'}),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/login/$', views.LoginView.as_view(template_name="django_registration/login.html"), {"next_page": '/'}), 
    url(r'^accounts/logout/$', views.LogoutView.as_view(),{"next_page": '/'} ), 
    url(r'^tinymce/', include('tinymce.urls')),
]
