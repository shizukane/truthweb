from audioop import reverse
from re import template
from django.urls import re_path as url , include , path
from . import views
from .forms import CommentForm
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^sites/$', views.sites, name= 'sites'),
    url(r'^portfolio/$', views.portfolio, name= 'portfolio'),
    url(r'^magazine/$', views.magazine, name= 'magazine'),
    url(r'^homepage/$', views.homepage, name= 'homepage'),
    url(r'^blog/$', views.blog, name= 'blog'),
    url(r'^reset/$', views.reset, name= 'reset'),
    url(r'^help/$', views.help, name= 'help'),
    url(r'^socialmedia/$', views.socialmedia, name= 'socialmedia'),
    url(r'^landingpage/', views.landingpage, name= 'landingpage'),
    url(r'^ecommerce/', views.ecommerce, name= 'ecommerce'),
    url(r'^choices/$', views.choices, name= 'choices'),
    url(r'^search/', views.search_projects, name='search_results'),
    url(r'^project/(\d+)', views.get_project, name='project_results'),  
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^accounts/profile/$', views.user_profiles, name='profile'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    url(r'^comment/(\d+)', views.comment,name='comments'),

     

     


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)