
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/generate', methods=['GET', 'POST'])
def generate():
    output = ""
    if request.method == 'POST':
        output = request.json
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
