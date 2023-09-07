from flask import Flask, url_for, redirect, render_template, request
import pickle
import numpy as np

#create an instance of flask 
app = Flask(__name__)


#create a base route
@app.route('/')
def home():
    prediction = request.args.get('prediction')
    return render_template('home.html', prediction=prediction)

@app.route('/about')
def about():
    return render_template('about.html')
model =pickle.load (open ('rf_model_final', "rb"))
#predict route
@app.route("/predict", methods=["POST"])
#@app.route('/predict', methods=["POST","GET"])
#def predict():
    #if request.method == 'POST':
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = np.array([int_features])
    prediction=model.predict(final_features)
        #budget = request.form['budget']
        
        # Let's load the package
    #def predict():
        #int_features = [int(x) for x in request.form.values()]
        #final_features = np.array([int_features])
        #prediction=model.predict(final_features)
        #output = round(prediction[0], 2)
    

        #model =pickle.load (open ('rf_model_final', "rb"))
        #prediction= model.predict([[int(prediction)]])
        #prediction=int(prediction[0])
    #prediction = {'0' : 'satilmamistir', '1': 'satilmistir'}
    if prediction == 1:
        prediction ="sold"
    else:
        prediction = "unsold"
    return redirect(url_for('home',
                prediction=f'This product has been {prediction}'))
        #model = pickle.load(open('simple_linear_regression.pkl', 'rb'))
        #prediction = model.predict([[int(budget)]])
        #prediction = int(prediction[0])
        #return redirect(url_for('home',
                #prediction=f'Predicted Sales Amount: {prediction}Millions'))
        
        # >>> person = {'name': 'Eric', 'age': 74} >>> "Hello, {name}. You are {age}.".format(**person) 'Hello, Eric. You are 74.'

if __name__ == '__main__':
    app.run(debug=False)