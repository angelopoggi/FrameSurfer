from samsungtvws import SamsungTVWS

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

    def send_to_tv(self, file_name):
        with open(file_name, 'rb') as tv_file:
            data = tv_file.read()
            upload = self.tv.art().upload(data, file_type='JPEG')
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
