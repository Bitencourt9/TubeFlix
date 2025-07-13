from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('watch/<int:video_id>/', views.watch_video, name='watch_video'),
    path('upload/', views.upload_video, name='upload_video'),
    path('profile/', views.user_profile, name='user_profile'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('like/<int:video_id>/', views.like_video, name='like_video'),
]

