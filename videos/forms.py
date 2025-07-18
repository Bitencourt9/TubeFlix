from django import forms
from .models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'file', 'thumbnail']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }