from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

urlpatterns = [
    path('admin/', user_passes_test(is_admin)(admin.site.urls)),
    path('api/auth/', include('users.urls')),
    path('api/vocab/', include('vocab.urls')),
    path('api/listening/', include('listening.urls')),
    path('api/level-test/', include('leveltest.urls')),
]