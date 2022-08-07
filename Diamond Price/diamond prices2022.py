import pickle
import numpy as np
from flask import render_template, request, jsonify, app, Flask
import sklearn

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('model.html')


@app.route('/predict', method=['POST','GET'])
def results():
    carat = float(request.form['carat'])
    cut = float(request.form['cut'])
    color = float(request.form['color'])
    clarity = float(request.form['clarity'])
    depth = float(request.form['depth'])
    table = float(request.form['table'])
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = float(request.form['z'])

    var = np.array([[carat, cut, color, clarity, depth, table, x, y, z]])
    model = pickle.load(open('model.pkl', 'rb'))
    y_predict = model.predict('var')
    return jsonify({'Prediction': float(Y_predict)})


if __name__ == '__main__':
    app.run(debug = True, port = 1010)
