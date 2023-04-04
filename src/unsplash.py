import requests
from src.creds import Creds

class UnSplash:
    def __init__(self):
        creds = Creds()
        self.client_id = creds.unsplash_creds()

    def fetch_random(self):
        '''
        Fetches a random photo link for download
        :return:
        '''
        url = 'https://api.unsplash.com/photos/random'
        header = {
            "Authorization": f"Client-ID {self.client_id}"
        }
        params = {
            'orientation' : 'landscape',
            'content_filter' : 'high'
        }
        response = requests.get(url,
                                headers=header,
                                params = params
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
        return file_name