from django.urls import path
from .views import VocabularyListCreateView, random_words, mark_word_known

urlpatterns = [
    path('', VocabularyListCreateView.as_view(), name='vocab-list-create'),
    path('random/', random_words, name='vocab-random'),
    path('mark/', mark_word_known, name='vocab-mark'),
]
