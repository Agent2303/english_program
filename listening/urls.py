from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ListeningTaskListView, ListeningTaskDetailView, submit_answer

urlpatterns = [
    path('', ListeningTaskListView.as_view(), name='listening-list'),
    path('<int:pk>/', ListeningTaskDetailView.as_view(), name='listening-detail'),
    path('answer/', submit_answer, name='listening-answer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
