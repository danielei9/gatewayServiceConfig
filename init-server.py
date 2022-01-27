from flask import Flask, render_template
from flask import *
import cambiarIp
import cambiarAp
import getConfig
import os

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
# #
#Routes
# #
@app.route('/')
def home():
    return render_template('index.html')

# allow both GET and POST requests
@app.route('/config', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'GET':
        var = getConfig.getConfig()
        print(var)
        return var
    if request.method == 'POST':
        inputIP = request.form.get('inputIP')
        inputDIN = request.form.get('inputDIN')
        inputSSID = request.form.get('inputSSID')
        inputPSWD = request.form.get('inputPSWD')
        inputPEP = request.form.get('inputPEP')
        print(inputIP)
        cambiarIp.changeIp(inputIP, inputDIN, inputPEP)
        cambiarAp.changeAp(inputSSID, inputPSWD)
        os.system('sudo reboot')
        return "reboot"
    return "No POST"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7777, debug=True)