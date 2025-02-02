from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import pickle
import traceback

model=pickle.load(open('CustomerSatisfaction','rb'))
app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
         Onlineboarding=request.form['Onlineboarding']
         Inflightentertainment=request.form['Inflightentertainment']
         Seatcomfort=request.form['Seatcomfort']
         onboardservicen=request.form['Onboardservice']
         Legroomservice=request.form['Legroomservice']
         cleanliness=request.form['cleanliness']
         FlightDistance=request.form['FlightDistance']
         Inflightwifiservice=request.form['Inflightwifiservice']
         #datanew=np.array([[Onlineboarding,Inflightentertainment,Seatcomfort,onboardservicen,Legroomservice,cleanliness,FlightDistance,Inflightwifiservice]]),

        # التنبؤ
         prediction=model.predict([[Onlineboarding,Inflightentertainment,Seatcomfort,onboardservicen,Legroomservice,cleanliness,FlightDistance,Inflightwifiservice]])
        #probability = model.predict_proba(datanew)
    
         result = "راضٍ" if prediction[0] == 1 else "غير راضٍ"
         return render_template("index.html",predict=result)
        
    

if __name__ == '__main__':
    app.run(debug=True)
