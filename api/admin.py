from django.contrib import admin
from api.models import Task

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_completed', 'created_at']
    list_display_links = ['id', 'title']

admin.site.register(Task, TaskModelAdmin)