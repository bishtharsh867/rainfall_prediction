from flask import Flask, render_template, request

import pickle
from PIL import Image,ImageTk
import numpy as np
import os


app = Flask(__name__, template_folder='templates', static_folder='static')



app = Flask(__name__)

model = pickle.load(open('rainfall_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    pressure = float(request.form['pressure'])
    wind = float(request.form['wind_speed'])
    
    data = np.array([[temp, humidity, pressure, wind]])
    prediction = model.predict(data)[0]
    
    return render_template('index.html', 
                           prediction_text=f"Predicted Rainfall: {prediction:.2f} mm")

if __name__ == "__main__":
    app.run(debug=True)
