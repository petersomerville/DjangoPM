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



def create_proj(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        title = request.POST['html_title']

        Project.objects.create(
            user_id = user_id,
            title = title
        )
        return redirect('proj_manager:index')
    return render(request, 'proj_manager/index.html')

def delete_proj(request, proj_id):
    project = Project.objects.get(id = proj_id)
    project.delete()
    return redirect('proj_manager:index')

def edit_proj(request, proj_id):
    context = {
        'project' : Project.objects.get(id = proj_id)
    }
    return render(request, 'proj_manager/edit_proj.html', context)

def update_proj(request, proj_id):
    if request.method == 'POST':
        project = Project.objects.get(id = proj_id)
        project.title = request.POST['html_title']
        project.save()

        return redirect('proj_manager:index')
    return render(request, 'proj_manager/index.html')

def register(request):
    if 'user_id' in request.session:
        return redirect('proj_manager:index')
    if request.method == 'POST':
        if len(request.POST['html_email']) > 0 and request.POST['html_password'] == request.POST['html_confirm']:
            try:
                user = User.objects.create(email = request.POST['html_email'], password = request.POST['html_password'])
                request.session['user_id'] = user.id
                request.session['email'] = user.email
            except:
                messages.error(request, 'Account already in use')
                return redirect('proj_manager:register')

        return redirect('proj_manager:index')
    return render(request, 'proj_manager/register.html')

def login(request):
    if 'user_id' in request.session:
        return redirect('proj_manager:index')
    if request.method == 'POST':
        try:
            user = User.objects.get(email = request.POST['html_email'])
            if request.POST['html_password'] == user.password:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                return redirect('proj_manager:index')
            else:
                messages.error(request, 'Invalid login')
                return redirect('proj_manager:login')
        except:
            messages.error(request, 'Invalid login')
            return redirect('proj_manager:login')

    return render(request, 'proj_manager/login.html')

def logout(request):
    request.session.clear()
    return redirect('proj_manager:index')


