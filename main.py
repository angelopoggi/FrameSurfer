from src.unsplash import UnSplash
from src.samsung import FrameSurfer

if __name__ == "__main__":
    photo_generator = UnSplash()
    photo_file = photo_generator.fetch_random()
    frame_tv = FrameSurfer(
        tv_address='192.168.1.154'
    )
    #save the file name that was uplaoded to the TV. The TV autogeneartes one such as MY_F123
    tv_file_name = frame_tv.send_to_tv(file_name=photo_file)
    #Set the actual picture on your TV
    frame_tv.set_picture(tv_file_name=tv_file_name)