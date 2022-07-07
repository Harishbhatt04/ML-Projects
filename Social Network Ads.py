import numpy as np
import pickle
from flask import Flask, render_template,request, jsonify
import sklearn

app = Flask(__name__)

@ app.route('\')

def home()

return render_template('index.html')

@app.route('/predict',method = ['POST''GET'])
def result():

x1 = float(request.form['Age'])
x2 = float(request.form['EstimatedSalary'])
x3 = float(request.form['gender_male'])

X = np.array([x1,x2,x3])
model = pickle.load(open('model.pkl','rb'))
y_predict = model.predict(X)
return jsonify ({'prediction':float(y_predict)})


if__name__=='__main__':
app.run(debug=True,port = 1010)






