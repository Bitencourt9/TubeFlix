from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from videos.models import Video
from .models import Comment
from django.contrib import messages

@login_required
def add_comment(request, video_id):
    if request.method == 'POST':
        video = Video.objects.get(id=video_id)
        text = request.POST.get('text')
        if text:
            Comment.objects.create(user=request.user, video=video, text=text)
    return redirect('watch_video', video_id=video_id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.user:
        if request.method == 'POST':
            comment.delete()
            messages.success(request, 'Comentário deletado com sucesso!')
            return redirect('user_profile')
        else:

            messages.error(request, 'Método não permitido para deletar comentário. Use o botão de deletar.')
            return redirect('user_profile')
    else:
        messages.error(request, 'Você não tem permissão para deletar este comentário.')
        return redirect('user_profile')
