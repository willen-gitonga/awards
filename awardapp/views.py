from django.shortcuts import render, redirect
from .models import Project,UsabilityRating,ContentRating,DesignRating
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewProjectForm,DesignForm,UsabilityForm,ContentForm


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
    return render(request, 'new-project.html', {"form": form, "user": current_user})


# @login_required(login_url='/accounts/login')
# def rate_project(request, project_id):
#     project = Project.objects.get(pk=project_id)
#     profile = User.objects.get(username=request.user)
#     if request.method == 'POST':
#         rateform = RateForm(request.POST, request.FILES)
#         print(rateform.errors)
#         if rateform.is_valid():
#             rating = rateform.save(commit=False)
#             rating.project = project
#             rating.user = request.user
#             rating.save()
#             return redirect(home)
#     else:
#         rateform = RateForm()
#     return render(request, 'rate.html', locals())
@login_required(login_url='/accounts/login')
def add_usability(request, project_id):
    rati = UsabilityRating.objects.filter(project_id=project_id)
    project = Project.objects.get(pk=project_id)
    profile = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = UsabilityForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = project
            rating.user = request.user
            rating.save()
        return redirect('homePage')
    else:
        form = UsabilityForm()

    return render(request, 'usability.html',locals())

@login_required(login_url='/accounts/login')
def add_design(request, project_id):
    rato = DesignRating.objects.filter(project_id=project_id)
    project = Project.objects.get(pk=project_id)
    profile = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = project
            rating.user_name = request.user
            rating.save()
        return redirect('homePage')
    else:
        form = DesignForm()
    return render(request, 'design.html',locals())
@login_required(login_url='/accounts/login')
def add_content(request,  project_id):
    rates = ContentRating.objects.filter(project_id=project_id)
    project = Project.objects.get(pk=project_id)
    profile = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = project

            rating.user_name = request.user
            rating.save()

        return redirect('homePage')
    else:
        form = ContentForm()

    return render(request, 'content.html',locals())
