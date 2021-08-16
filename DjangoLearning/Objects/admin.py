from django.contrib import admin
from .models import demirbasobje

# Register your models here.

@admin.register(demirbasobje)

class demirbasobjeAdmin(admin.ModelAdmin):
    list_display = ["title", "no", "author", "created_date"]
    search_fields = ["no"]
    list_filter = ["created_date"]
    class Meta:
        model = demirbasobje


