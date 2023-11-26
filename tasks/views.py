from django.shortcuts import render

# Create your views here.
tasks = ['Study Django', 'Study Docker', 'Study Kubernetes']

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
    