from django.shortcuts import render, redirect
from apps.proj_manager.models import Project, Task

# Create your views here.

def index(request):
    if 'user_id' in request.session:
        context = {
            'projects' : Project.objects.filter(user_id = request.session['user_id'])
        }
        return render(request, 'proj_manager/index.html', context)
    return redirect('proj_manager:login')

def create_project(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        title = request.POST['html_title']

        Project.objects.create(
            user_id = user_id,
            title = title
        )
        return redirect('proj_manager:index')
    return render(request, 'proj_manager/index.html')

def delete_project(request, proj_id):
    project = Project.objects.get(id = proj_id)
    project.delete()
    return redirect('proj_manager:index')

def edit_project(request, proj_id):
    context = {
        'project' : Project.objects.get(id = proj_id)
    }
    return render(request, 'proj_manager/edit_project.html', context)

def update_project(request, proj_id):
    if request.method == 'POST':
        project = Project.objects.get(id = proj_id)
        project.title = request.POST['html_title']
        project.save()

        return redirect('proj_manager:index')
    return render(request, 'proj_manager/index.html')

