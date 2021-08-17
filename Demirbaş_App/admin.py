from django.contrib import admin

# Register your models here.
from .models import Worker, Device

admin.site.register(Worker)
admin.site.register(Device)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["id", "person", "created_date"]
    search_fields = ["id", "person", "created_date"]
    list_filter = ["created_date"]
    class Meta:
        model = Worker

