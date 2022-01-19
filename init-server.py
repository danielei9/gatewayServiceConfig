from flask import Flask, render_template
from flask import *
import cambiarIp
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
@app.route('/')
def home():
    return render_template('index.html')
# allow both GET and POST requests
@app.route('/config', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        inputIP = request.form.get('inputIP')
        inputDIN = request.form.get('inputDIN')
        inputSSID = request.form.get('inputSSID')
        inputPSWD = request.form.get('inputPSWD')
        inputPEP = request.form.get('inputPEP')
        print(inputIP)
        cambiarIp.changeIp(inputIP, inputDIN, inputPEP)
        return '''
                  <h1>The value is: {}</h1>
                  <h1>The value is: {}</h1>'''.format(inputIP, inputDIN)
    return "No POST"
if __name__ == '__main__':
   app.run(host='localhost', port=8000, debug=True)