from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import pickle
from datetime import datetime
import os

app = Flask(__name__)

# Load the trained model and scaler
model = load_model('Secure-Learning-Management-System-with-Content-Encryption-and-Student-Performance-Prediction/final_marks_predictor_model.h5')
with open('Secure-Learning-Management-System-with-Content-Encryption-and-Student-Performance-Prediction/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# CSV file configuration
CSV_FILENAME = 'student_predicted_performance.csv'

def init_csv():
    """Initialize CSV file with headers if it doesn't exist"""
    if not os.path.exists(CSV_FILENAME):
        headers = ['name', 'age', 'year1_marks', 'year2_marks', 'study_time', 
                  'failures', 'predicted_score', 'timestamp']
        pd.DataFrame(columns=headers).to_csv(CSV_FILENAME, index=False)

def save_to_csv(data):
    """Save prediction data to CSV file"""
    try:
        # If file doesn't exist, create it with headers
        if not os.path.exists(CSV_FILENAME):
            init_csv()
        
        # Append new data to CSV
        df = pd.DataFrame([data])
        df.to_csv(CSV_FILENAME, mode='a', header=False, index=False)
        return True
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return False

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
        return predicted_marks[0][0]
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Log the incoming form data
        print("Received form data:", request.form)

        # Retrieve form data
        name = request.form['name']
        age = int(request.form['age'])
        year1_marks = float(request.form['year1_marks'])
        year2_marks = float(request.form['year2_marks'])
        studytime = float(request.form['study_time'])
        failures = int(request.form['failures'])

        # Predict final marks
        prediction = predict_new_input(model, scaler, age, year1_marks, year2_marks, studytime, failures)

        if prediction is None:
            print("Prediction returned None.")
            return jsonify({'error': 'Prediction failed due to internal error.'}), 500
        
        # Round the prediction to 2 decimal places
        rounded_prediction = round(float(prediction), 2)
        
        # Log the prediction result
        print(f"Prediction result: {rounded_prediction}")

        # Prepare data for CSV storage
        data = {
            'name': name,
            'age': age,
            'year1_marks': year1_marks,
            'year2_marks': year2_marks,
            'study_time': studytime,
            'failures': failures,
            'predicted_score': rounded_prediction,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # Save to CSV
        if not save_to_csv(data):
            return jsonify({'error': 'Error saving data to CSV.'}), 500

        # Return the result as a JSON response
        return jsonify({'prediction': rounded_prediction})
    
    except KeyError as ke:
        print(f"KeyError: {ke}")
        return jsonify({'error': f'Missing required field: {ke}'}), 400
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return jsonify({'error': 'Invalid input. Please ensure all fields contain correct values.'}), 400
    except Exception as e:
        print(f"Error during form submission: {e}")
        return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    init_csv()  # Initialize CSV file when starting the application
    app.run(debug=True)



    