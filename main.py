
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data.get('prompt', '')
        # Here you can add any processing logic for the prompt
        return jsonify({'content': prompt})
    return jsonify({'error': 'Invalid request method'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
