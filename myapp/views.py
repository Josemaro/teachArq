from django.http import HttpResponse, JsonResponse
from . import models
from django.shortcuts import get_object_or_404
# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World!</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1>")

def projects(request):
    projects = list(models.Project.objects.values())
    return JsonResponse(projects,safe=False)

def project(request, id):
    try:
        project = models.Project.objects.get(id=id)
        return HttpResponse(project.name)
    except:
        return HttpResponse(f"Project with id {id} not found")
    
def tasks(request):
    tasks = list(models.Task.objects.values())
    return JsonResponse(tasks,safe=False)

def task(request, id):
    try:
        task = models.Task.objects.get(id=id)
        return HttpResponse(task.title)
    except:
        return HttpResponse(f"Tasks with id {id} not found")