from django.urls import re_path as url , include , path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^sites/$', views.sites, name= 'sites'),
    url(r'^reset/', views.password_reset_request, name= 'reset'),
    url(r'^search/', views.search_projects, name='search_results'),
    url(r'^project/(\d+)', views.get_project, name='project_results'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^accounts/profile/$', views.user_profiles, name='profile'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings') ),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    path('reset/password_reset_done.html', auth_views.PasswordResetDoneView.as_view(template_name='django_registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="django_registration/password_reset_confirm.html"), name='password_reset_confirm',), 
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='django_registration/password_reset_complete.html'), name='password_reset_complete'),      

     


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)