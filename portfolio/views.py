from django.shortcuts import render
from .models import Project
from blog.models import Blog
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


def home(request):

    projects = Project.objects.order_by('-dateProject')
    blogs = Blog.objects.order_by('-dateBlog')[:3]
    
    paginator = Paginator(projects, 3)
    #length = int(request.GET.get('length', 12))
    
    numProjects = 0
    page = request.GET.get('page')
    

    project = paginator.get_page(page)

    numProjects = len(project)

    

    return render(request, 'portfolio/home.html', {'projects': project,'blogs': blogs,'numProjects': numProjects})

def detailProject(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    return render(request, 'portfolio/detail.html', {'project': project})


def contact(request):

    return render(request, 'portfolio/contact.html')
