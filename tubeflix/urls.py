from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from videos import views as video_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hub.urls')),
    path('videos/', include('videos.urls')),
    path('comments/', include('comments.urls')),
    path('users/', include('users.urls')),
    path('search/', video_views.search_videos, name='search_videos'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)