from flask import Flask, render_template, url_for, request, send_from_directory
import numpy as np
import pandas as pd
import joblib

# translate Flask to python object
server = Flask(__name__,static_url_path='', 
            static_folder='web')

@server.route("/")
def home():
    return render_template("index.html")

@server.route("/predict")
def predict():
    return render_template("predict.html")


@server.route("/statistic")
def statistic():
    return render_template("statistic.html")


@server.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
       input = request.form

       df = pd.DataFrame({
           'city':[input['city']],
           'city_development_index':[input['city_development_index']],
           'gender':[input['gender']],
           'relevent_experience':[input['relevent_experience']],
           'enrolled_university':[input['enrolled_university']],
           'education_level':[input['education_level']],
           'major_discipline':[input['major_discipline']],
           'experience':[input['experience']],
           'company_size':[input['company_size']],
           'company_type':[input['company_type']],
           'last_new_job':[input['last_new_job']],
           'training_hours':[input['training_hours']],
       })
       
       
    model = joblib.load("ModelJoblib")

    prediksi = model.predict_proba(df)

    if prediksi[0][1] < 0.5:
        result = 'NOPE!! Tidak Mencari Pekerjaan Baru'
        return render_template('result.html', data=input, pred=result,hasil=prediksi)
        
    else:
        result = 'YUP!! Akan Mnecari Pekerjaan Baru'
        return render_template('result.html', data=input, pred=result,hasil=prediksi)   


if __name__ == '__main__':
    model = joblib.load("ModelJoblib")
    server.run(debug=True, port=1212)
