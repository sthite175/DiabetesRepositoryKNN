from flask import Flask,render_template,request,jsonify
from utilities import diabetes_prediction
import pickle
import config

app=Flask(__name__)    # Home page
@app.route("/")
def app_home():
    return render_template("index.html")

@app.route("/prediction",methods=["post"])
def get_prediction():
    # It fatches dictionary from the HTML
    data=request.form
    pred_output=diabetes_prediction(data)

    #return jsonify({"Result":diabetes})   # It will for postman result for checking app will work or not
    return render_template("index.html",Result=pred_output) # We have to write code in index.html 

# code run the app
if __name__=="__main__":
    app.run(debug=True,port=config.PORT,host=config.HOST)
    
