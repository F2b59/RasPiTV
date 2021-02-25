#!/usr/bin/python3
import os
from flask import Flask, render_template, render_template_string, redirect, request
from time import sleep
app = Flask(__name__)


import channels # list of channels

ch = []  # list of char


### TO DO: REWORK INDENTATION


@app.route('/')
def index():
    global ch
    templateData = {
        'title': 'Remote Controller',
        'ch': 'Selection : ' + ''.join(ch),
        'error': ''
    }
    if len(ch) == 2:
        try:
            channel = ''.join(ch)
            channel = channels.List[channel - 1][0] # get the address of the stream
            os.system('killall omxplayer.bin')
            os.system('nohup omxplayer --live -o alsa:hw:CARD=Device %s > nohup.out 2> nohup.err < /dev/null &') % channel
            ch = []
        except:
            templateData['error'] = 'Failed to play video'
            ch = []
    elif len(ch) == 1:
            tmp = ch.copy()
            sleep(2) # waiting time
            if ch == tmp:
                try:
                    channel = ''.join(ch)
                    channel = channels.List[channel - 1][0] # get the address of the stream
                    os.system('killall omxplayer.bin')
                    os.system('nohup omxplayer --live -o alsa:hw:CARD=Device %s > nohup.out 2> nohup.err < /dev/null &') % channel
                    ch = []
                except:
                    templateData['error'] = 'Failed to play video'
                    ch = []
    return render_template('index.html', **templateData)


@app.route('/setch', methods=['POST'])
def setCh():
    global ch
    ch.append(request.form["ch_select"])
    return redirect(request.referrer)


@app.route('/shutdown', methods=['POST'])
def shutDown():
    templateData = {
        'title': 'Remote Controller',
        'ch': '',
        'error': ''
    }
    try:
        os.system('sudo shutdown -h now')
    except:
        templateData['error'] = 'Failed to shut down'
        return render_template('index.html', **templateData)
    templateData['ch'] = 'Shut Down'
    return render_template('index.html', **templateData)


@app.route('/reboot', methods=['POST'])
def reboot():
    templateData = {
        'title': 'Remote Controller',
        'ch': '',
        'error': ''
    }
    try:
        os.system('sudo reboot')
    except:
        templateData['error'] = 'Failed to reboot'
        return render_template('index.html', **templateData)
    templateData['ch'] = 'Reboot'
    return render_template('reboot.html', **templateData)


@app.route('/stop', methods=['POST'])
def stop():
    templateData = {
        'title': 'Remote Controller',
        'ch': '',
        'error': ''
    }
    try:
        os.system('killall omxplayer.bin')
    except:
        templateData['error'] = 'Failed to kill OMXPlayer'
        return render_template('index.html', **templateData)
    return redirect(request.referrer)


@app.route('/list')
def displayList():
    return '\n'.join([channels.List[i][0] + ', ' + channels.List[i][1] for i in range(len(channels.List))])


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
