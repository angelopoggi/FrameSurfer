from django.contrib import admin
from .models import FrameTV, UnsplashModel, PhotoModel

# Register your models here.
@admin.register(UnsplashModel)
class UnsplashAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "oauth_token")

@admin.register(FrameTV)
class FrameTVAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "ip_address",
        "api_service",
        "topics",
        "matte_options"
    )

@admin.register(PhotoModel)
class PhotoModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "downloaded_at",
        "url",
        "tv"
    )
