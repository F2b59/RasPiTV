#!/usr/bin/python3
import os
from flask import Flask, render_template, render_template_string, redirect, url_for, request, send_from_directory
from time import sleep
app = Flask(__name__)


from channels import chList # list of channels
from logos import logo # list of logos

ch = []  # list of char
templateData = {
    'title': 'Remote Controller',
    'ch': 'Selection : ' + ''.join(ch),
    'error': ''
}

for line in logo[0]:
    print(line)
os.system('hostname -I')

@app.route('/favicon.ico') # from https://stackoverflow.com/questions/48863061/favicon-ico-results-in-404-error-in-flask-app
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


def play(url):
    # Old command, using OMXplayer (deprecated starting from Debian 11)
    #command = 'nohup omxplayer --live -o alsa:hw:CARD=Device ' + url + ' > nohup.out 2> nohup.err < /dev/null &'
    # Now, it is recommended to use VLC
    # Please change the user if it's not "pi"
    command = 'nohup sudo -u pi cvlc --alsa-audio-device hw:CARD=Device --play-and-exit "' + url + '" > nohup.out 2> nohup.err < /dev/null &'
    os.system(command)


@app.route('/')
def index():
    global ch
    global templateData
    
    if len(ch) == 2:
        channelNb = int(''.join(ch))
        try:
            channel = chList[channelNb - 1][0] # get the address of the stream
        except:
            templateData['error'] = 'Channel Index out of range'
            templateData['ch'] = ''
            ch = []
            return render_template('index.html', **templateData)
        stop() #os.system('killall omxplayer.bin')
        try:
            for line in logo[channelNb]:
                print(line)
        except:
            print("Starting stream of channel " + str(channelNb))
        play(channel)
        templateData['ch'] = 'Selection : ' + ''.join(ch)
        ch = []
    
    elif len(ch) == 1:
        tmp = ch.copy()
        sleep(1.5) # waiting time
        if ch == tmp:
            channelNb = int(''.join(ch))
            channel = chList[channelNb - 1][0] # get the address of the stream
            stop() #os.system('killall omxplayer.bin')
            try:
                for line in logo[channelNb]:
                    print(line)
            except:
                print("Starting stream of channel " + str(channelNb))
            play(channel)
            templateData['ch'] = 'Selection : ' + ch[0]
            ch = []
    
    templateData['error'] = ''
    return render_template('index.html', **templateData)


@app.route('/setch', methods=['POST'])
def setCh():
    global ch
    ch.append(request.form["ch_select"])
    return redirect(request.referrer)


@app.route('/custom', methods=['POST'])
def customStream():
    global templateData
    url = request.form["addr"]
    yt_dl = request.form["yt"]
    stop()
    print(str(yt_dl)) #debug
    if yt_dl == "0":
        play(url)
    else:
        #os.system('nohup omxplayer --live -o alsa:hw:CARD=Device $(youtube-dl -g -f "(mp4)[height<=480]" ' + url + ') > nohup.out 2> nohup.err < /dev/null &') # remove the height<=480 condition for full size
        play('$(youtube-dl -g -f "(mp4)[height<=480]" ' + url + ')') # à tester
    templateData['ch'] = 'Selection : ' +  url
    return redirect(request.referrer)


@app.route('/shutdown', methods=['POST'])
def shutDown():
    global templateData
    stop()
    os.system('nohup $(sleep 0.2 && shutdown -h now) &')
    templateData['ch'] = 'Shut Down'
    return redirect(request.referrer)


@app.route('/reboot', methods=['GET']) # not used
def reboot():
    global templateData
    stop()
    os.system('nohup $(sleep 0.2 && reboot) &')
    templateData['ch'] = 'Reboot'
    return redirect(request.referrer)


@app.route('/stop', methods=['POST'])
def stop():
    # if using OMXplayer, simply replace "vlc" by "omxplayer.bin"
    global templateData
    templateData['ch'] = 'Selection : '
    try:
        os.system('killall vlc')
    except:
        templateData['ch'] = ''
        templateData['error'] = 'Failed to kill VLC'
        return render_template('index.html', **templateData)
    return redirect(request.referrer)


@app.route('/list')
def displayList():
    html = '<html>\n<body>\n\n'
    html += '<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">\n<title>Liste des chaînes</title>\n<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">\n<style>body{height:100%;margin:5%;color:#f0f0f0;background-color:#333333;font-family:\'IBM Plex Sans\',sans-serif;align-items:left;}</style>\n</head>\n'
    html += '<body>\n\n<b><a href="/">Retour</a></b><br>\n'
    html += '<br>\n'.join([str(i+1) + ' - ' + chList[i][1] + ' - ' + chList[i][0] for i in range(len(chList))])
    html += '\n\n</body>\n</html>'
    return   html


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
