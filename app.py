import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import os

# Create flask app
app = Flask(__name__)

# Load the model with exception handling
model_path = "RF.pkl"
if os.path.exists(model_path):
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading the model: {e}")
        model = None
else:
    print(f"Model file not found at {model_path}")
    model = None

@app.route("/")
def Home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return render_template("index.html", prediction_text="Model not loaded properly.")
    
    try:
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        prediction_text = f"The booking status is: {'Cancelled' if prediction == 1 else 'Not Cancelled'}"
    except Exception as e:
        prediction_text = f"Error making prediction: {e}"
    
    return render_template("index.html", prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)