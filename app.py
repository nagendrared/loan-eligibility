from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pickle
import numpy as np

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# The rest of your Flask code...

# Load the trained model
with open('loan_eligibility_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/favicon.ico')
def favicon():
    return "", 204


@app.route('/')
def home():
    return "Loan Eligibility Prediction API is running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()
        feature_values = [
            data.get("income"),
            data.get("loan_amount"),
            data.get("credit_score"),
            data.get("self_employed"),
            data.get("property_area"),
            data.get("loan_term"),
            
        ]

        # Ensure all features are numeric (some preprocessing may be needed)
        feature_array = np.array([feature_values], dtype=float)

        # Make prediction using the loaded modeln
        prediction = model.predict(feature_array)

        # Check prediction and send response
        if prediction == 1:
            return jsonify({'eligible': True})
        else:
            return jsonify({'eligible': False})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
