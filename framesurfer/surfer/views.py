from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import TVForm, APIServiceForm
from .models import FrameTV, UnsplashModel, PhotoModel
from .api_utils import UnSplash
import os


def add_api_service(request):
    if request.method == 'POST':
        form = APIServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('api_service_list')
    else:
        form = APIServiceForm()
    return render(request, 'surfer/add_api_service.html', {'form': form})

def api_service_list(request):
    api_services = UnsplashModel.objects.all()
    return render(request, 'surfer/api_service_list.html', {'api_services': api_services})

def add_tv(request):
    if request.method == 'POST':
        form = TVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tv_list')
    else:
        form = TVForm()
    return render(request, 'surfer/add_tv.html', {'form': form})

def tv_list(request):
    tvs = FrameTV.objects.all()
    return render(request, 'surfer/tv_list.html', {'tvs': tvs})


def download_photo(request, tv):
    if request.method == "POST":
        tv_object = get_object_or_404(FrameTV, id=tv)
        print(tv_object.ip_address)
        unsplash = UnSplash(tv_object)
        #before downloading anything - check to see if folder even exists
        if not os.path.exists(f"{settings.BASE_DIR}/photos/{tv_object.name}"):
            os.makedirs(f"{settings.BASE_DIR}/photos/{tv_object.name}")
        unsplash.fetch_random(file_path=f"{settings.BASE_DIR}/photos/{tv_object.name}")
        return redirect('tv_list')
    return redirect('tv_list')
    # headers = {
    #     'Authorization': f'Client-ID {tv.api_service.oauth_token}'
    # }
    # topics = tv.topics.split(',')
    # response = requests.get(f'{tv.api_service.api_url}/random?query={topics[0]}', headers=headers)
    # if response.status_code == 200:
    #     data = response.json()
    #     photo_url = data['urls']['regular']
    #     photo = PhotoModel.objects.create(url=photo_url, tv=tv)
    #     tv_ip = tv.ip_address
    #     requests.post(f'http://{tv_ip}/display', json={'photo_url': photo_url})
    #     return photo
    # return None

def downloaded_photos(request):
    photos = PhotoModel.objects.all()
    return render(request, 'surfer/downloaded_photos.html', {'photos': photos})