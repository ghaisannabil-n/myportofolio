from django.shortcuts import render

from main.models import Experience

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

# Create your views here.
