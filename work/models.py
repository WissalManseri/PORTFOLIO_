from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    #  FileField pour stocker le fichier PDF
    cv = models.FileField(upload_to="cv_files/", default='False')

    def __str__(self):
        return self.name

class Education(models.Model):
    school_name = models.CharField(max_length=255)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField()
    is_current = models.BooleanField(default=False)
class Experience(models.Model):
    position = models.CharField(max_length=255)
    start_month = models.CharField(max_length=255, blank=True, null=True)
    end_month = models.CharField(max_length=255, blank=True, null=True)
    is_current = models.BooleanField(default=False)
    end_year = models.IntegerField(blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    description = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=255)
    proficiency = models.IntegerField()

#project

class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(default='')

class ProjectAi(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(default='')
    is_ai_project = models.BooleanField(default=False)  # Marqueur pour les projets IA
    pdf_file = models.FileField(upload_to='project_pdfs/', blank=True, null=True)

# blog and certificate
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    #category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    #pub_date = models.DateTimeField()
    pub_date = models.DateField()
    def __str__(self):
        return self.title

#contact

class ContactMessage(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.email}"