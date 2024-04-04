from django.contrib import admin
from .models import FarmingEquipment
# Register your models here.
admin.site.register(FarmingEquipment)
def add_info(modeladmin, request, queryset):
    for obj in queryset:
        obj.additional_info = "Some additional information"
        obj.save()
add_info.short_description = "Add additional info"
class YourModelAdmin(admin.ModelAdmin):
    actions = [add_info]
