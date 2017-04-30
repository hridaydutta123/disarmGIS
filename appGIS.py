from flask import Flask
from flask import request
from flask import Flask, request, render_template
	
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['files']
        f.save('./static/heatvals.js')
        return '200'
    else:
        return 'Upload Page'

if __name__ == '__main__':
#    app.debug = True
    app.run()
