from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract and convert input values from form
        features = [
            float(request.form['age']),
            float(request.form['study_hours_per_day']),
            float(request.form['social_media_hours']),
            float(request.form['netflix_hours']),
            int(request.form['part_time_job']),
            float(request.form['attendance_percentage']),
            float(request.form['sleep_hours']),
            int(request.form['diet_quality']),
            int(request.form['exercise_frequency']),
            int(request.form['parental_education_level']),
            int(request.form['internet_quality']),
            int(request.form['mental_health_rating']),
            int(request.form['extracurricular_participation'])
        ]

        # Convert to 2D array as expected by model
        input_array = np.array([features])
        prediction = model.predict(input_array)[0]

        # Round prediction to 2 decimal places
        prediction = round(prediction, 2)

        return render_template('index.html', prediction=prediction)
    
    except Exception as e:
        print("Error during prediction:", e)
        return render_template('index.html', prediction="Error in input or model prediction.")

if __name__ == '__main__':
    app.run(debug=True)
