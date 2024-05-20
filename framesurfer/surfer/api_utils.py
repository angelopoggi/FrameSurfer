import datetime

import requests
from PIL import Image
from .models import PhotoModel
from samsungtvws import SamsungTVWS

class UnSplash:
    def __init__(self, tv_object):
        self.tv = tv_object
    def _resize_image(self, image_path):
        # Open the image
        img = Image.open(image_path)

        # Calculate the target aspect ratio dimensions for 16:9
        original_width, original_height = img.size
        target_width = original_width
        target_height = int(target_width * (9 / 16))

        # Check if the new height is larger than the original height
        if target_height > original_height:
            # Scale down width to fit the original height
            target_height = original_height
            target_width = int(target_height * (16 / 9))

        # Calculate cropping area to maintain center
        left = (original_width - target_width) // 2
        top = (original_height - target_height) // 2
        right = left + target_width
        bottom = top + target_height

        # Crop the image to maintain a 16:9 aspect ratio
        cropped_img = img.crop((left, top, right, bottom))

        # Resize the image to the specified dimensions (3840x2160)
        resized_img = cropped_img.resize((3830, 2100))

        # Save the image
        resized_img.save(image_path)

    def fetch_random(self, file_path):
        '''
        Fetches a random photo link for download
        :return:
        '''
        url = 'https://api.unsplash.com/photos/random/?w=3840&h=2160&topics=WdChqlsJN9c,6sMVjTLSkeQ&content_filter=high&orientation=landscape'
        header = {
            "Authorization": f"Client-ID {self.tv.api_service.oauth_token}"
        }
        # params = {
        #     'orientation' : 'landscape',
        #     'content_filter' : 'high',
        #     'topcis' : "WdChqlsJN9c"
        # }
        response = requests.get(url,
                                headers=header,
                                #params = params
                                )
        if response.status_code == 200:
            data = response.json()
            #download file
            with requests.get(data['links']['download'],stream=True) as download_response:
                with open(f"{file_path}/{data['id']}.jpg", 'wb') as file:
                    #save information about the photo
                    photo = PhotoModel.objects.create(
                        name=data['id'],
                        downloaded_at=datetime.datetime.now(),
                        url=data['urls']['raw'],
                        tv=self.tv
                    )
                    photo.save()
                    for chunk in download_response.iter_content(1024):
                        file.write(chunk)
                        file_name = file.name
        else:
            raise Exception(f'Error: {response.status_code}')
        #resize the image
        self._resize_image(file_name)

class FrameSurfer:
    def __init__(self,tv_address):
        self.tv_address = tv_address
        self.tv = SamsungTVWS(self.tv_address)
    def _check_power(self):
        '''checks to see if the TV is in the ON state'''
        info_output = self.tv.rest_device_info()
        if info_output['device']['PowerState'] == 'on':
            return True
        else:
            return False

    def _check_art_mode(self):
        '''check to see if the TV is in Art Mode'''
        info_output = self.tv.art().get_artmode()
        if info_output == 'on':
            return True
        else:
            return False

    def send_to_tv(self, file_name, matte=None):
        with open(file_name, 'rb') as tv_file:
            data = tv_file.read()
            upload = self.tv.art().upload(data, matte=matte, file_type='JPEG')
        return upload

    def set_picture(self, tv_file_name):
        power_check = self._check_power()
        art_check = self._check_art_mode()
        if power_check == True and art_check == True:
            self.tv.art().select_image(tv_file_name)
        elif power_check == True and art_check == False:
            self.tv.art().select_image(tv_file_name, show=False)
        else:
            self.tv.art().select_image(tv_file_name, show=False)
    def change_to_artmode(self):
        art_check = self._check_art_mode()
        if art_check == False:
            self.tv.art().set_artmode(True)
