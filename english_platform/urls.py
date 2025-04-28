from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.cache import never_cache

admin.site.login = never_cache(user_passes_test(lambda u: u.is_active and u.is_staff)(admin.site.login))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/vocab/', include('vocab.urls')),
    path('api/listening/', include('listening.urls')),
    path('api/level-test/', include('leveltest.urls')),
]