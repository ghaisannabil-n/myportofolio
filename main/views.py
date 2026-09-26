from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        

from main.models import Experience
from main.models import Education
from main.forms import ProjectForm
from main.models import Project
from main.forms import ExperienceForm
import datetime

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Ghaisan Nabil Iradat",
        "npm": "2506619051",
        "study_program": "S1 Sistem Informasi",
        "bio": ("Mahasiswa Fakultas Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
        "last_login" : last_login,
    }
    return render(request, "index.html", context)

def show_education(request):
    context = {
        "name": "Nabil",
        "education_list": Education.objects.all()
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied("Akses ditolak: Developer Only")
     
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil diinisiasi!")
        return redirect("main:show_projects")

    context = {
        "name": "Nabil",
        "form": form,
    }
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied("Akses ditolak: Developer Only")
    
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience berhasil ditambahkan!")
        return redirect("main:show_experience")
    
    context = {
        "name" : "Nabil",
        "form" : form,
    }
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_ = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_:
        experience = experience.filter(title_icontains = title_)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied("Akses ditolak: Developer Only")
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience Berhasil Dihapus!")
        return redirect("main:show_experience")
    
    return redirect("main:show_experience")
    
def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Nabil",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def show_experience(request):
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experience = [experience.object for experience in experience]
    title_query= request.GET.get("title", "").strip()

    context = {
        "name": "Nabil",
        "experience_list": experience,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize(
        "json", projects, use_natural_foreign_keys=True 
    )
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied("Akses ditolak: Developer Only")
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def edit_project(request, project_id):
    is_editor = request.user.groups.filter(name="Editor").exists()
    if not (request.user.is_superuser or is_editor):
        raise PermissionDenied("Akses ditolak: Developer Only")
    
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek berhasil diubah!")
        return redirect("main:show_projects")

    context = {"name": "Ghaisan Nabil", "form": form}
    return render(request, "projects_form.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

# Create your views here.

