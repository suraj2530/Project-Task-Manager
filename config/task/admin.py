from django.contrib import admin
from .models import Project, Task, Reminder, Comment


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Reminder)
admin.site.register(Comment)