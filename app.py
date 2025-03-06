from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        cgpa = float(request.form['cgpa'])
        iq = int(request.form['iq'])

        # Make prediction
        prediction = model.predict([[cgpa, iq]])[0]

        # Convert prediction to human-readable output
        result = "Placed ✅" if prediction == 1 else "Not Placed ❌"

        return render_template('index.html', result=result)
    
    except:
        return render_template('index.html', result="Invalid Input ❌")

if __name__ == '__main__':
    app.run(debug=True)
