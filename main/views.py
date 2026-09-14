from django.shortcuts import render

from main.models import Experience
from main.models import Education

def show_main(request):
    context = {
        "name" : "Ghaisan Nabil Iradat",
        "npm" : "2506619051",
        "study_program" : "S1 Sistem Informasi",
        "bio" : ("Mahasiswa Fakultas Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Nabil",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "smp" : "SMPIT AT-TAUFIQ",
        "sma" : "MAN 15 JAKARTA",
        "kuliah" : "Universitas Indonesia"
        "education_list" : Education.objects.all(),
    }


# Create your views here.
