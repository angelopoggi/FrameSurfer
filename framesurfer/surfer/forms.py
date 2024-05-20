from django import forms
from .models import FrameTV, UnsplashModel

class APIServiceForm(forms.ModelForm):
    class Meta:
        model = UnsplashModel
        fields = ['name', 'url', 'oauth_token']

class TVForm(forms.ModelForm):
    class Meta:
        model = FrameTV
        fields = ['name', 'ip_address', 'api_service', 'topics', 'matte_options']