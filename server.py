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

@app.route('/shutdown')
def shutDown():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('sudo shutdown -h now')
        except:
                return 'error'
        return render_template('index.html', **templateData)

@app.route('/reboot')
def reboot():
        message = ''
        templateData = {
                'result' : message
        }
        try:
                os.system('sudo reboot')
        except:
                return 'error'
        return render_template('index.html', **templateData)

if __name__=='__main__':
        app.run(debug=True, port=80, host='0.0.0.0')