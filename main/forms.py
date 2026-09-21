from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project
from main.models import Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
            "experience_img",
        ]

        labels = {
            "title": "Name of Experience",
            "description": "Description of Experience",
            "category": "Category",
            "thumbnail": "Thumbnail",
            "started_at": "Tahun Awal",
            "ended_at": "Tahun Akhir",
            "experience_image": "URL Experience",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "started_at": TextInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "ended_at": TextInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "experience_img": URLInput(
                attrs={
                    "placeholder": "",
                }
            ),
        }