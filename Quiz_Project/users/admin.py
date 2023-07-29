from django.contrib import admin
from .models import *

@admin.register(LoginLogs)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','user_type','login_at')
