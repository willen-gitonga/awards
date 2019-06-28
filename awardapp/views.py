from django.shortcuts import render,redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewProjectForm


@login_required(login_url='/accounts/login/')
def home(request):
    projects = Project.get_all_projects()

    return render(request, 'index.html', {"projects": projects})


@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    # try:
    #     current_profile = Profile.objects.get(user_id=id)
    # except ObjectDoesNotExist:
    #     return redirect(update_profile, current_user.id)

    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect(home)

    else:
        form = NewProjectForm()
    return render(request, 'new-project.html', {"form": form,"user":current_user})
