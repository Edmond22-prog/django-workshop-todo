from django.contrib import admin

from core.models import TodoTask


@admin.register(TodoTask)
class TodoTaskAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title", "completed", "deleted", "updated_date")
    list_filter = ("completed", "deleted")
    list_editable = ("completed", "deleted")
