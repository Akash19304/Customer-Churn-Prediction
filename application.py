from flask import Flask, request, render_template
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')


application=Flask(__name__)
app=application 

model = pickle.load(open('model/customer_churn_model.pkl','rb'))

@app.route('/')
def home_page():
    return render_template('form.html')

@app.route('/predict', methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        tenure=float(request.form.get('Tenure'))
        MonthlyCharges=float(request.form.get('MonthlyCharges'))
        gender = 1 if str(request.form.get('gender'))=='Male' else 0
        SeniorCitizen = 1 if str(request.form.get('SeniorCitizen'))=='Yes' else 0
        Partner = 1 if str(request.form.get('Partner'))=='Yes' else 0
        Dependents = 1 if str(request.form.get('Dependents'))=='Yes' else 0
        PhoneService = 1 if str(request.form.get('PhoneService'))=='Yes' else 0
        MultipleLines = 1 if str(request.form.get('MultipleLines'))=='Yes' else 0
        InternetService = 1 if str(request.form.get('InternetService'))=='Yes' else 0
        OnlineSecurity = 1 if str(request.form.get('OnlineSecurity'))=='Yes' else 0
        OnlineBackup = 1 if str(request.form.get('OnlineBackup'))=='Yes' else 0
        DeviceProtection = 1 if str(request.form.get('DeviceProtection'))=='Yes' else 0
        TechSupport = 1 if str(request.form.get('TechSupport'))=='Yes' else 0
        StreamingTV = 1 if str(request.form.get('StreamingTV'))=='Yes' else 0
        StreamingMovies = 1 if str(request.form.get('StreamingMovies'))=='Yes' else 0
        PaperlessBilling = 1 if str(request.form.get('PaperlessBilling'))=='Yes' else 0

        con = str(request.form.get('Contract')) 
        if con=='Month-to-month':
            Contract=0
        elif con=='One year':
            Contract=1
        else:
            Contract=2

        payment = str(request.form.get('PaymentMethod'))
        if payment=='Bank transfer (automatic)':
            PaymentMethod=0
        elif payment=='Credit card (automatic)':
            PaymentMethod=1
        elif payment=='Electronic check':
            PaymentMethod=2
        else:
            PaymentMethod=3

        input = np.array([gender, SeniorCitizen, Partner, Dependents, tenure,
                        PhoneService, MultipleLines, InternetService, OnlineSecurity,
                        OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
                        StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
                        MonthlyCharges])
        
        result= model.predict([input])
        if result[0]==0:
            final_result='Yes'
        else:
            final_result='No'

        return render_template('form.html', results=final_result)
    else:
        return render_template('form.html')
    

if __name__ == "__main__":  
    app.run()
        

        