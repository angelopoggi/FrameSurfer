from django.urls import path
from . import views

urlpatterns = [
    path('api_service/add/', views.add_api_service, name='add_api_service'),
    path('api_service/', views.api_service_list, name='api_service_list'),
    path('tv/add/', views.add_tv, name='add_tv'),
    path('tv/', views.tv_list, name='tv_list'),
    #pass in the TV idea
    path('tv/download_photo/<int:tv>/', views.download_photo, name='download_photo'),
    path('photos/', views.downloaded_photos, name='downloaded_photos'),
]