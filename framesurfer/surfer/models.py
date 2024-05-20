from django.db import models
#from django_cryptography.fields import encrypt

class UnsplashModel(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField()
    oauth_token = models.CharField(max_length=256)

    def __str__(self):
        return self.url

class FrameTV(models.Model):
    name = models.CharField(max_length=256)
    ip_address = models.GenericIPAddressField(protocol="both", blank=True, null=True)
    api_service = models.ForeignKey(UnsplashModel, on_delete=models.CASCADE, related_name="api_service")
    topics = models.TextField(help_text="Comma-sperated list of topcis", blank=True, null=True)
    matte_options = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name

class PhotoModel(models.Model):
    name = models.CharField(max_length=256)
    downloaded_at = models.DateTimeField(auto_now=True)
    url = models.URLField()
    tv = models.ForeignKey(FrameTV, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.name

