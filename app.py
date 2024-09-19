from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import pickle
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Load the trained model and scaler
try:
    model = load_model('final_marks_predictor_model.h5')
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    logging.info("Model and scaler loaded successfully")
except Exception as e:
    logging.error(f"Error loading model or scaler: {e}")

def predict_new_input(model, scaler, age, year1_marks, year2_marks, studytime, failures):
    try:
        new_input = pd.DataFrame({
            'age': [age],
            'year1_marks': [year1_marks],
            'year2_marks': [year2_marks],
            'studytime': [studytime],
            'failures': [failures]
        })
        new_input_scaled = scaler.transform(new_input)
        predicted_marks = model.predict(new_input_scaled)
        logging.info(f"Prediction successful: {predicted_marks[0][0]}")
        return predicted_marks[0][0]
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        logging.info(f"Received form data: {request.form}")

        age = int(request.form['age'])
        year1_marks = float(request.form['year1_marks'])
        year2_marks = float(request.form['year2_marks'])
        studytime = float(request.form['study_time'])
        failures = int(request.form['failures'])

        prediction = predict_new_input(model, scaler, age, year1_marks, year2_marks, studytime, failures)

        if prediction is None:
            logging.error("Prediction returned None.")
            return jsonify({'error': 'Prediction failed due to internal error.'}), 500
        
        rounded_prediction = round(float(prediction), 2)
        logging.info(f"Prediction result: {rounded_prediction}")

        return jsonify({'prediction': rounded_prediction})
    
    except KeyError as ke:
        logging.error(f"KeyError: {ke}")
        return jsonify({'error': f'Missing required field: {ke}'}), 400
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return jsonify({'error': 'Invalid input. Please ensure all fields contain correct values.'}), 400
    except Exception as e:
        logging.error(f"Error during form submission: {e}")
        return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)