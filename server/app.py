from flask import Flask, request
import model
import numpy as np
from preprocess import preprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
classifier = model.load_model()

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/predict', methods=['POST'])
def predict():
    raw_data = dict(request.get_json())
    payload = raw_data['payload']
    input = preprocess(payload)
    prediction = np.exp(classifier.predict(input)[0])
    return str(prediction)

if __name__ == '__main__':    
    app.run(port=8080, host='0.0.0.0', debug=True)
