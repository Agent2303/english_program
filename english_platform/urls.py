from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/vocab/', include('vocab.urls')),
    path('api/listening/', include('listening.urls')),
    path('api/level-test/', include('leveltest.urls')),
]