from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projects(request):
    return HttpResponse('Here are the projects')

def project(request, pk):
    return HttpResponse('Single project ' + str(pk) )