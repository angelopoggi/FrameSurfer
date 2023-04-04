# FrameSurfer

This is a simple library intended to download a random photo from unsplash and uploaded it to the SamsungFrame TV.
Since there are no known ways (at least that i've looked up) to display a new image or cycle through them, this will do it for you.

This is still a work in progress but the current code works as is.

You will need the following

* Unsplash Key (can be obtained by creating a free developer account)
* Samsung Frame TV (not free, unless it was for you ;) )

## How to use

First you'll need to create a .env file under `/src` as such

```commandline
UNSPLASH_KEY=<your key here>
```
once the file is genearted and key is set you can use the `main.py` as an example and substiture your IP Address of the TV.
You should consider using the DNS name of the TV or setting a fixed IP on your DHCP server (most likely your home router if running at home)

```python
from src.unsplash import UnSplash
from src.samsung import FrameSurfer

if __name__ == "__main__":
    #initializes the UnSplash class
    photo_generator = UnSplash()
    #Get a random photo 
    photo_file = photo_generator.fetch_random()
    #make a connection to the TV
    frame_tv = FrameSurfer(
        tv_address='192.168.1.165'
    )
    #save the file name that was uplaoded to the TV. The TV autogeneartes one such as MY_F123
    tv_file_name = frame_tv.send_to_tv(file_name=photo_file)
    #Set the actual picture on your TV
    frame_tv.set_picture(tv_file_name=tv_file_name)
```

# Planned features
No commitments on these but the following ideas are floating around in my head

* ability to use other photo services
* ability to run as a CLI tool (click?)
* Run inside a docker container

If you are interested in adding features, please feel free to request or make the code changes yourself and do a pull request!

Thanks!