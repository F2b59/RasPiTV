#!/usr/bin/python3
import os
from flask import Flask, render_template, render_template_string, redirect, url_for, request, send_from_directory
from time import sleep
app = Flask(__name__)


import channels # list of channels
import logos # list of logos

ch = []  # list of char

for line in logos.raspitv:
    print(line)
os.system('hostname -I')

@app.route('/favicon.ico') # from https://stackoverflow.com/questions/48863061/favicon-ico-results-in-404-error-in-flask-app
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    global ch
    templateData = {
        'title': 'Remote Controller',
        'ch': 'Selection : ' + ''.join(ch),
        'error': ''
    }
    if len(ch) == 2:
        channel_nb = int(''.join(ch))
        try:
            channel = channels.List[channel_nb - 1][0] # get the address of the stream
        except:
            templateData['error'] = 'Index out of range'
            ch = []
            return render_template('index.html', **templateData)
        stop() #os.system('killall omxplayer.bin')
        for line in logos.List[channel_nb - 1]:
            print(line)
        os.system('nohup omxplayer --live -o alsa:hw:CARD=Device ' + channel + ' > nohup.out 2> nohup.err < /dev/null &')
        ch = []
    elif len(ch) == 1:
        tmp = ch.copy()
        sleep(1.5) # waiting time
        if ch == tmp:
            channel_nb = int(''.join(ch))
            channel = channels.List[channel_nb - 1][0] # get the address of the stream
            stop() #os.system('killall omxplayer.bin')
            for line in logos.List[channel_nb - 1]:
                print(line)
            os.system('nohup omxplayer --live -o alsa:hw:CARD=Device ' + channel + ' > nohup.out 2> nohup.err < /dev/null &')
            ch = []
    return render_template('index.html', **templateData)


@app.route('/setch', methods=['POST'])
def setCh():
    global ch
    ch.append(request.form["ch_select"])
    return redirect(request.referrer)


@app.route('/custom', methods=['POST'])
def customStream():
    url = request.form["addr"]
    yt_dl = request.form["yt"]
    stop()
    print(str(yt_dl)) #debug
    if yt_dl == "0":
        os.system('nohup omxplayer --live -o alsa:hw:CARD=Device ' + url + ' > nohup.out 2> nohup.err < /dev/null &')
    else:
        os.system('nohup omxplayer --live -o alsa:hw:CARD=Device $(youtube-dl -g -f mp4 ' + url + ') > nohup.out 2> nohup.err < /dev/null &')
    templateData = {
        'title': 'Remote Controller',
        'ch': 'Selection : ' +  url,
        'error': ''
    }
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
    return render_template('index.html', **templateData)


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
    return '<html>\n<body>\n\n' + '<br>\n'.join([str(i+1) + ' - ' + channels.List[i][1] + ' - ' + channels.List[i][0] for i in range(len(channels.List))]) + '\n\n</body>\n</html>'


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
