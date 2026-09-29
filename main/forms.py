from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput, ValidationError

from main.models import Project
from main.models import Experience
from django.utils.html import strip_tags

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
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh berisi tag HTML.")
        return title
    
    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()
    
    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip() 

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
            "started_at": DateInput(
                attrs={
                    "placeholder": "",
                }
            ),
            "ended_at": DateInput(
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