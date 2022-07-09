
from dataclasses import fields
from re import template
from unicodedata import category
from xml.etree.ElementTree import Comment
from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.shortcuts import get_object_or_404

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.db.models import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from .models import Profile,Projects,Comment
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,RegisterForm,NewProjectForm,CommentForm
from django.contrib import messages
from rest_framework.response import Response
from django.core.mail import BadHeaderError, send_mail
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer
from django.contrib.auth.forms import PasswordResetForm


# Create your views here.

def index(request):

    return render(request, 'index.html')
def portfolio(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    return render(request, 'portfolio.html',{"date": date, "projects":projects})
def homepage(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    return render(request, 'homepage.html',{"date": date, "projects":projects})
def blog(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    return render(request, 'blog.html',{"date": date, "projects":projects})
def magazine(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    return render(request, 'magazine.html',{"date": date, "projects":projects})
def choices(request):

    return render(request, 'choices.html')
def sites(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    return render(request, 'sites.html',{"date": date, "projects":projects})
def landingpage(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    return render(request, 'landingpage.html',{"date": date, "projects":projects})
def ecommerce(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    return render(request, 'ecommerce.html',{"date": date, "projects":projects})
def socialmedia(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    return render(request, 'socialmedia.html',{"date": date, "projects":projects})
def help(request):

    return render(request, 'help.html')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/')
        
    else:
        form = RegisterForm()
    return render(request, 'django_registration/registration_form.html', {'form':form})
    
    
@login_required(login_url='/accounts/login/')
def search_projects(request):
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_projects = Projects.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


def get_project(request, id):

    try:
        project = Projects.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()
    
    
    return render(request, "projects.html", {"project":project})
  

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Author = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new-project.html', {"form": form})
def reset(request):

    return render(request,'django_registration/reset.html' )

@login_required(login_url='/accounts/login/')
def user_profiles(request):
    current_user = request.user
    Author = current_user
    projects = Projects.get_by_author(Author)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
     

        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
        
    else:
        form = ProfileUpdateForm()
    
    return render(request, 'django_registration/profile.html', {"form":form, "projects":projects})
def password_reset_request(request):
    if request.method == "POST":
        domain = request.headers['Host']
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "django_registration/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': domain,
                        'site_name': 'Interface',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("password_reset_done.html")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="django_registration/reset.html",
                  context={"password_reset_form": password_reset_form})
def comment(request, id):
    form_class = CommentForm
    form = form_class(request.POST)
    if request.method == 'POST':
      if form.is_valid():
            form.save()
    else:
        form = CommentForm()
    try:
        comments = Comment.objects.get(pk = id)
        
    except ObjectDoesNotExist:
        raise Http404()
      
    return render(request, "comments.html", {"form":form, 'comments':comments},{"next_page": '/'})
class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = Projects.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)
    
    
class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()
        serializers = ProfileSerializer(all_profile, many=True)
        return Response(serializers.data)


    