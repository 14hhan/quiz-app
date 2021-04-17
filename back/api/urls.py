from django.urls import path, include
from .views import randomQuiz

urlpatterns = [
    path('quizs/<int:id>/', randomQuiz),
]
