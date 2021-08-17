from django.contrib import admin

# Register your models here.
from .models import Worker

@admin.register(Worker)
class ÇalışanAdmin(admin.ModelAdmin):
    list_display = ["person", "status", "exp", "created_date"]
    search_fields = ["person", "status", "exp", "created_date"]
    list_filter = ["created_date"]
    class Meta:
        model = Worker