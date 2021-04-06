# RasPiTV -- A RPi-based TV box #

Use OMXPlayer to play video streams on your TV with the RaspberryPI, and control it with your phone.

## Why this project ##
If you're looking for a way of watching TV via you're RaspberryPi, you must already know about Kodi or other media centers. They provide pretty much any feature you might want, together with a beautiful UI. But maybe it's not what you want. Maybe you just have a set of web TV streams that you want to play without having to go through multiple menus. Also, maybe your RaspberryPi is not fast enough to run a media center without lag.
If it's the case, then you're at the right place. Because that's exactly what I needed myself. 

I developed this small Python program for my RaspberryPi Zero W and a standard definition screen ; for HD, it might be worth consedering a more powerful RPi.
This program was originally based on daaanny90's Remote-Raspberry project, which introduced me to Flask and served as a model for mine.

## Installation ##
I'm assuming you're using Raspberry Pi OS (aka Raspbian)
1. Clone the repo into your Raspberry Pi's home folder.
2. Install Flask if not already installed with `sudo pip install flask`
3. Add "python3 /home/pi/RasPiTV/server.py" to your /etc/rc.local file
4. Strongly recommended : increase GPU memory to at least 128MB (I set it to 192MB for my Pi Zero W but feel free to try other values)
5. As this program is taylored for my own configuration, you might want to modify the omxplayer command (for example, remove the `-o alsa:hw:CARD=Device` parameter)
6. Put your streams in `channels.py`. The file `channels_hd.py` isn't used by the program by default. You can put ASCII-style logos in `logos.py`
7. If you plan to play videos from Youtube, download and install the last version of [Youtube-dl](https://youtube-dl.org/)

**Important notes**
* If you did follow the steps above, then the server starts automatically on startup. It is run **as root**. I know this isn't good practice. You can run it with another user, but the shutdown command might not work.
* The streams addresses in the files `channels.py` and `channels_hd.py` are French TV streams from https://github.com/HugoPoi/9boxtv. They are here as an example. It's not free content ; use them only if you have the right to do so.

## How to use it ##
When the server is running, you can reach the frontend writing the IP address of your Raspberry Pi on the browser. This address is given under the __RasPiTV__ logo at startup.

This is what you will see (from a smartphone):
![RaspberryPi Remote Controller Screenshot](/screenshot/Screenshot_20210406_120313.jpg "RasPiTV web interface")

Just press a button to start watching TV.
I suggest to give a static IP to your Pi and put a shortcut on the home screen of your phone.

If you want to play a custom stream, paste the link and click on __Submit custom stream__.
If you want to play a Youtube video, paste the link to that video and click on __Submit Youtube video__. It will use youtube-dl to get the MP4 link that will be given to OMXPlayer. Please note that this can take some time.
