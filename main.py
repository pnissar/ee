from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
pipe=pickle.load(open("ri.pkl",'rb'))
app=Flask(__name__)
data=pd.read_csv('c.csv')
@app.route('/')

def index():
    l=sorted(data['location'].unique())
    return render_template('index.html',l=l)
@app.route('/predict',methods=['POST'])
def predict():
    lo=request.form.get('loc')
    bhk=request.form.get('bhk')
    bath=request.form.get('bath')
    sqrt=request.form.get('sqrt')
    input=pd.DataFrame([[lo,sqrt,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    # print(input.describe())
    p=pipe.predict(input)*1e5
    return str(np.round(p[0],2))
if __name__=="__main__":
    app.run(debug=True,port=5001)