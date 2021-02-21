#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)
import os

@app.route('/')
def index():
        templateData = {
                'title' : 'Remote Controller'
        }
        return render_template('index.html', **templateData)

@app.route('/shutdown.html')
def shutDown():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('sudo shutdown -h now')
        except:
                return 'error'
        return render_template('shutdown.html', **templateData)

@app.route('/reboot.html')
def reboot():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('sudo reboot')
        except:
                return 'error'
        return render_template('reboot.html', **templateData)

@app.route('/stop.html')
def stop():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('killall omxplayer.bin')
        except:
                return 'error'
        return render_template('stop.html', **templateData)

@app.route('/01.html')
def ch01():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('/home/pi/remote-raspberry/channels/01.sh')
        except:
                return 'error'
        return render_template('01.html', **templateData)

@app.route('/02.html')
def ch02():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('/home/pi/remote-raspberry/channels/02.sh')
        except:
                return 'error'
        return render_template('02.html', **templateData)

@app.route('/03.html')
def ch03():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('/home/pi/remote-raspberry/channels/03.sh')
        except:
                return 'error'
        return render_template('03.html', **templateData)

@app.route('/04.html')
def ch04():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('/home/pi/remote-raspberry/channels/04.sh')
        except:
                return 'error'
        return render_template('04.html', **templateData)

@app.route('/05.html')
def ch05():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('/home/pi/remote-raspberry/channels/05.sh')
        except:
                return 'error'
        return render_template('05.html', **templateData)

@app.route('/06.html')
def ch06():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('/home/pi/remote-raspberry/channels/06.sh')
        except:
                return 'error'
        return render_template('06.html', **templateData)

@app.route('/07.html')
def ch07():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('/home/pi/remote-raspberry/channels/07.sh')
        except:
                return 'error'
        return render_template('07.html', **templateData)

@app.route('/08.html')
def ch08():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('/home/pi/remote-raspberry/channels/08.sh')
        except:
                return 'error'
        return render_template('08.html', **templateData)

@app.route('/09.html')
def ch09():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('/home/pi/remote-raspberry/channels/09.sh')
        except:
                return 'error'
        return render_template('09.html', **templateData)

if __name__=='__main__':
        app.run(debug=True, port=80, host='0.0.0.0')
