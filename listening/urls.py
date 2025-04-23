from django.urls import path
from .views import ListeningTaskListView, ListeningTaskDetailView, submit_answer

urlpatterns = [
    path('', ListeningTaskListView.as_view(), name='listening-list'),
    path('<int:pk>/', ListeningTaskDetailView.as_view(), name='listening-detail'),
    path('answer/', submit_answer, name='listening-answer'),
]
