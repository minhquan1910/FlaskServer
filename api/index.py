from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        req_data = request.get_json()
        name = req_data['name']
        return jsonify({'message': name})