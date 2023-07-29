from django.contrib import admin
from .models import *

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'exam')
    list_display_links = ('id', 'name')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'section')
    list_display_links = ('id', 'name')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','topic')
    list_display_links = ('id', 'title')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'quiz', 'marks')
    list_filter = ('quiz',)
    search_fields = ('title',)

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'question', 'is_correct')
    list_filter = ('question', 'is_correct')
    search_fields = ('title',)
