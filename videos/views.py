from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoUploadForm
from comments.forms import CommentForm
from comments.models import Comment
from django.contrib import messages
from comments.models import Comment
from django.db.models import Q
from .models import Video, Like


def watch_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.views += 1
    video.save()

    comments = Comment.objects.filter(video=video).order_by('created_at')

    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = Like.objects.filter(user=request.user, video=video).exists()

    if request.method == 'POST':

        comment_form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.video = video
                new_comment.user = request.user
                new_comment.save()
                messages.success(request, 'Seu comentário foi adicionado!')
                return redirect('watch_video', video_id=video.id)
            else:
                messages.error(request, 'Erro ao adicionar comentário. Por favor, tente novamente.')
        else:
            messages.warning(request, 'Você precisa estar logado para comentar.')
            return redirect('login')

    else:
        comment_form = CommentForm()

    outros_videos = Video.objects.exclude(id=video_id).order_by('?')[:5]

    context = {
        'video': video,
        'outros_videos': outros_videos,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'videos/watch.html', context)

def home(request):
    videos = Video.objects.all().order_by('-created_at')[:20]
    return render(request, 'hub/home.html', {'videos': videos})

@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('watch_video', video_id=video.id)
    else:
        form = VideoUploadForm()
    return render(request, 'videos/upload.html', {'form': form})

@login_required
def user_profile(request):
    user_videos = Video.objects.filter(user=request.user).order_by('-created_at')

    user_comments = Comment.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'user_videos': user_videos,
        'user_comments': user_comments,
    }
    return render(request, 'videos/user_profile.html', context)


@login_required
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if video.user != request.user:
        return redirect('user_profile')
    if request.method == 'POST':
        video.delete()
        return redirect('user_profile')
    return redirect('user_profile')

def search_videos(request):
    query = request.GET.get('q')
    videos = Video.objects.all()

    if query:

        videos = videos.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).distinct()

    context = {
        'query': query,
        'videos': videos,
    }
    return render(request, 'videos/search_results.html', context)


@login_required
def like_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    like_exists = Like.objects.filter(user=request.user, video=video).exists()
    if request.method == 'POST':
        if like_exists:
            Like.objects.filter(user=request.user, video=video).delete()
            messages.info(request, 'Você descurtiu o vídeo.')
        else:
            Like.objects.create(user=request.user, video=video)
            messages.success(request, 'Você curtiu o vídeo!')
        return redirect('watch_video', video_id=video.id)
    else:
        return redirect('watch_video', video_id=video.id)


