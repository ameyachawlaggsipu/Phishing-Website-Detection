from extractor import featureExtraction
from flask import Flask, render_template, request
import numpy as np
import pickle
app = Flask(__name__)
loaded_model = pickle.load(open("finalized_model (2).sav", 'rb'))

@app.route("/")
def home():
    return  render_template("index.html")

@app.route('/success', methods = ['POST']) 
def predict():
    text = request.form['text']
    features = featureExtraction(text)
    features = np.array(features)
    features = features.reshape((1,16))
    r = loaded_model.predict(features)
    if r == 1 :
        output = "Phishing Website"
    else :
        output = "Genuine Website"
    print(output)
    return  render_template("index2.html",data = output)
    
if __name__ == "__main__":
    app.run(debug=True)
