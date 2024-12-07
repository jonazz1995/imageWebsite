from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "created_at"]
    search_fields = ["title"]
