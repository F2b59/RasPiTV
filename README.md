# RasperryPi Remote Controller #

Use your smartphone as a remote controller for your RaspberryPi, to shutdown and reboot your device.

## Why this project ##
The RaspberryPi has no button to shut down or reboot the system. I use my Raspberry to as media center to watch television, and it's always on and connected to my television, also if I turn off the TV.

I didn't want to just cut the power to shut down my Raspberry, and I developed this little remote control with python and flask to properly shut down the system, in order to save power and extend the Raspberry's life.

## Installation ##
1. Clone the repo into your RaspberryPi
2. Install Flask if not already installed with `pip install flask`
3. Launch the server with `python server.py`

## How to use it ##
When the Flask server is running, you can reach the frontend writing the IP address of your RaspberryPi on the browser.

This is what you will see (from a smartphone):
![RaspberryPi Remote Controller Screenshot](/screenshot/RaspberryPi_remote_screenshot.png "RaspberryPi Remote Controller")

Just press the button to shut down or reboot your Raspberry!

I suggest to save this page on the home screen of your smartphone.

This is a really basic version and there is still a lot to do:

- [ ] Redirect when a button is pressed
- [ ] Add more controles