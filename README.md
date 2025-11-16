# 📊 Hotel-Cancellation-Analysis-and-Prediction
A Machine Learning Web App for Predicting Hotel Booking Cancellations

## ✅ Overview

This project is a complete end-to-end machine learning system designed to predict hotel reservation cancellations based on customer and booking details.
The workflow includes:

- Data preprocessing & feature engineering.
- Data Analysis using Python & SQL.
- Model training (Random Forest / Logistic Regression / KNN).
- Saving the best model using Pickle.
- Deploying prediction as a Flask web application.
- Interactive UI for prediction.

## 🧠 Tech Stack
### Data Analysis
- SQL
- Python Libraries (Matplotlib, Seaborn and Plotly)
### Machine Learning
- Scikit-learn
- NumPy
- pandas
### Model Deployment
- Flask
- Pickle (pickle library for serialization)
### Frontend
- HTML template (index.html)

## 📂 Project Structure
```bash
Hotel-Cancellation-Prediction/
│
├── app.py                                      # Flask backend app
├── RF.pkl                                      # Serialized pre-trained model
├── Hotel Cancellation Analysis and Prediction.ipynb   # Jupyter notebook (training + EDA)
│
├── templates/
│    └── index.html                             # Web UI for prediction
│
└── README.md                                   # Project documentation
```
## 🔗 Download the Model File

You can download the pre-trained model here:

👉 [Download RF.pkl](https://drive.google.com/file/d/1FAqrRkAWwGpJUbPIEAhTTIun9w-4e1Mj/view?usp=drive_link)

## 🚀 How It Works

### 1️⃣ Training Phase

Inside the notebook (Hotel Cancellation Analysis and Prediction.ipynb):

- Exploratory Data Analysis (EDA)

- Outlier handling & missing value treatment

- Feature encoding

- Model training:

  - Logistic Regression

  - KNN

  - Random Forest

- Model evaluation

- Saving the best model (Random Forest Model)

### 2️⃣ Deployment Phase

app.py loads the trained model:

- User inputs → Model predicts → UI displays result.

## ▶️ Run the Application Locally

### ✅ Step 1: Install dependencies
```bash
pip install -r requirements.txt
```
### ✅ Step 2: Ensure the model file exists
Place the trained model in the project root:
```bash
RF.pkl
```
### ✅ Step 3: Start the Flask server
```bash
python app.py
```
### ✅ Step 4: Open your browser
```bash
http://127.0.0.1:5000/
```

## 📈 Future Improvements

- Add interactive dashboard

- Deploy using Docker

- Create a RESTful API version

- Add model monitoring for real-time hotel systems

## 👩‍💻 Author

**Habiba M. Attia**
