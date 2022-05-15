from pydoc import pager
from .models import Project
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {"project": projectObj})