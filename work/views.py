from .models import *
from .models import ContactMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
def resume(request):
    user = User.objects.all()
    education_items = Education.objects.order_by('-end_year')
    # Order by end_year in descending order
    experience_items = Experience.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    # Filtrer les projets d'IA

    ai_projects = ProjectAi.objects.filter(is_ai_project=True)
    categories = Project.objects.values_list('category', flat=True).distinct()
    blog_posts = BlogPost.objects.order_by('pub_date').reverse()
    context = {

        'education_items': education_items,
        'user': user,
        'experience_items': experience_items,
        'skills': skills,
        'projects': projects,
        'ai_projects': ai_projects,
        'categories': categories,
        'blog_posts': blog_posts,
    }

    return render(request, 'index.html', context)
def contact_form(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Enregistrez le message dans la base de données
        ContactMessage.objects.create(fullname=fullname, email=email, message=message)

        messages.success(request, 'Your message has been sent successfully!')

    return redirect('index')  # Redirigez vers la page d'accueil
    return render(request, 'index.html')
