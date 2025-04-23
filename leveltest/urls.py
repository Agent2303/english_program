from django.urls import path
from .views import start_vocabulary_test, submit_vocabulary_test, start_listening_test, submit_listening_test, get_test_results

urlpatterns = [
    # Vocabulary Test
    path('vocabulary/start/', start_vocabulary_test, name='vocabulary-start'),
    path('vocabulary/submit/', submit_vocabulary_test, name='vocabulary-submit'),
    
    # Listening Test
    path('listening/start/', start_listening_test, name='listening-start'),
    path('listening/submit/', submit_listening_test, name='listening-submit'),
    
    # Test Natijalarini ko‘rish
    path('results/', get_test_results, name='test-results'),
]
