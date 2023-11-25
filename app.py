from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods = ['GET','POST'])
def hey():
    if request.method == 'POST':

        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        model = pickle.load (open('model.pkl'),'rb')
        user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict([[float(user_input)]])
        predicted_species = iris.target_names[prediction][0]

        return render_template('result.html', species=predicted_species)
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run()