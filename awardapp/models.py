from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from star_ratings.models import Rating
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'profile', blank=True, default='profile/default.png')

    def save_profile(self):
        self.save()
        
        img = Image.open(self.photo.path)
        if img.height > 200 or img.width > 200:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
            

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Projects(models.Model):
    project_title = models.CharField(max_length=255)
    project_image = models.ImageField(upload_to = 'images/', default='images/default.png')
    project_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    link = models.URLField()
    country = CountryField(blank_label='(select country)', default='RW')
    projectcategory = models.CharField(max_length=80)
    
    


    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects
    
    
    @classmethod
    def get_by_author(cls, Author):
        projects = cls.objects.filter(Author=Author)
        return projects
    
    
    @classmethod
    def get_project(request, id):
        try:
            project = Projects.objects.get(pk = id)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return project
    
    def __str__(self):
        return self.project_title
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'My Project'
        verbose_name_plural = 'Projects'
class Comment(models.Model):
    project = models.ForeignKey(Projects,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    Say_Something = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.project.project_title,self.name)