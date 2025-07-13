from django.shortcuts import render
from videos.models import Video

def home(request):
    videos = Video.objects.all().order_by('-created_at')[:20]
    return render(request, 'hub/home.html', {'videos': videos})
