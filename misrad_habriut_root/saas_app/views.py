# from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm
from django.contrib import messages
from django.db.models import Q
# from .utils import searchApps


# Create your views here.
# Decorators are added to restrict access to 
# function based views if not logged in / one of djangos stronger security features
# maybe put the internals of this view in another utils.py file...

@login_required(login_url='login')
def saas_app4(request):
    # apps, search_query = searchApps(request)
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    # filtering for tags because of tags' many to many relationship with apps/projects
    tags = Tag.objects.filter(name__icontains=search_query)

    # this section is the search functionality (.filter() instead of .get())
    apps = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    context = {'apps': apps, 'search_query':search_query}
    return render (request, 'saas_app4.html', context)

def single_saas_app(request, pk):
    # appObj = None
    # for i in appsList:
    #     if i['id'] == pk:
    #         appObj = i
    appObj = Project.objects.get(id=pk)
    return render(request, 'single_saas_app.html', {'app':appObj})


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()       
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('saas_app4')
    context = {'form': form}
    return render(request, 'project_form.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    # need some error hadnling here
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)       
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('saas_app4') 
    context = {'form': form}
    return render(request, 'project_form.html', context)


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'project was deleted!')
        return redirect('saas_app4')
    context = {'object': project}
    return render(request, 'delete_object.html', context)

@login_required(login_url='login')
def admin_approval(request):
    return render(request, 'admin_approval.html')








