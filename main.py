
from flask import Flask, render_template, jsonify, request
from langchain_google_genai import GoogleGenerativeAI

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
        print("initialising...")
        llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
        print("invoking...")
        result = llm.invoke("Gnerate an article for title: ", prompt)
        return jsonify({'content': result})
    return jsonify({'error': 'Invalid request method'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
