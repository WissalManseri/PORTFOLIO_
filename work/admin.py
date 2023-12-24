from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)

class EducationAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'start_year', 'end_year']

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'start_month', 'end_year','start_year', 'end_month', 'is_current']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency']

admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'link']

class ProjectAiAdmin(admin.ModelAdmin):
    list_display = ['title',  'pdf_file']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectAi, ProjectAiAdmin)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    search_fields = ['title']

admin.site.register(BlogPost, BlogPostAdmin)

#contact
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'timestamp')
    search_fields = ['fullname', 'email']

admin.site.register(ContactMessage, ContactMessageAdmin)