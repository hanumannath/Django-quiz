from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'exams', ExamViewSet)
router.register(r'exam/(?P<exam_id>\d+)/sections', SectionViewSet, basename='exam-sections')
router.register(r'section/(?P<section_id>\d+)/topics', TopicViewSet, basename='section-topics')
router.register(r'topic/(?P<topic_id>\d+)/quizzes', QuizViewSet, basename='topic-quizzes')
router.register(r'quiz/(?P<quiz_id>\d+)/questions', QuestionViewSet, basename='quiz-questions')

urlpatterns = [
    path('', include(router.urls)),
]
