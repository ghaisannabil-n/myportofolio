from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience
from main.models import Education
from main.forms import ProjectForm
from main.models import Project
from main.forms import ExperienceForm

def show_main(request):
    context = {
        "name": "Ghaisan Nabil Iradat",
        "npm": "2506619051",
        "study_program": "S1 Sistem Informasi",
        "bio": ("Mahasiswa Fakultas Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    json_response = get_experience_json(request)

    experience = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    experience = [experience.object for experience in experience]
    title_ = request.GET.get("title", "").strip()

    context = {
        "name": "Nabil",
        "experience_list": experience,
        "title_": title_,
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "name": "Nabil",
        "education_list": Education.objects.all()
    }
    return render(request, "education.html", context)

def create_project(request):
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

def create_experience(request):
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

def delete_experience(request, experience_id):
    experience = get_object_or_404(Project, ex=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Project Berhasil Dihapus!")
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

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

# Create your views here.

