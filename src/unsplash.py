import requests
from src.creds import Creds
from PIL import Image

class UnSplash:
    def __init__(self):
        creds = Creds()
        self.client_id = creds.unsplash_creds()

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

    def fetch_random(self):
        '''
        Fetches a random photo link for download
        :return:
        '''
        url = 'https://api.unsplash.com/photos/random/?w=3840&h=2160&topics=WdChqlsJN9c,6sMVjTLSkeQ&content_filter=high&orientation=landscape'
        header = {
            "Authorization": f"Client-ID {self.client_id}"
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
                with open(f"photos/{data['id']}.jpg", 'wb') as file:
                    for chunk in download_response.iter_content(1024):
                        file.write(chunk)
                        file_name = file.name
        else:
            raise Exception(f'Error: {response.status_code}')
        #resize the image
        self._resize_image(file_name)
        return file_name