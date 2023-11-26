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
        print("hhhhhhhhhhhhh ",sepal_length)
        model = pickle.load(open('model.pkl','rb'))
        
        user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(user_input)
        if(prediction==0):
            predicted_species = "Iris-setosa"
        elif(prediction==1):
            predicted_species = "Iris-versicolor"
        else:
            predicted_species = "Iris-virginica"

       
    
    return render_template('index.html', predicted_species==predicted_species)



if __name__ == '__main__':
   app.run(debug=True)