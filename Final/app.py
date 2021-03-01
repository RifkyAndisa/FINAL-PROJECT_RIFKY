from flask import Flask, render_template, url_for, request, send_from_directory
import numpy as np
import pandas as pd
import folium
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
       city = int(input['city'])
       city_development_index = float(input['city_development_index'])
       gender = int(input['gender'])
       relevent_experience = int(input['relevent_experience'])
       enrolled_university = int(input['enrolled_university'])
       education_level = int(input['education_level'])
       major_discipline = int(input['major_discipline'])   
       experience = int(input['experience'])
       company_size = int(input['company_size'])
       company_type = int(input['company_type'])
       last_new_job = int(input['last_new_job']) 
       training_hours = int(input['training_hours'])   
       
       df_predicts = pd.DataFrame({city : int(input['city']),
       city_development_index : float(input['city_development_index']),
       gender : int(input['gender']),
       relevent_experience : int(input['relevent_experience']),
       enrolled_university : int(input['enrolled_university']),
       education_level : int(input['education_level']),
       major_discipline : int(input['major_discipline']),  
       experience : int(input['experience']),
       company_size : int(input['company_size']),
       company_type : int(input['company_type']),
       last_new_job : int(input['last_new_job']), 
       training_hours : int(input['training_hours'])},index=[0])  
       
    model = joblib.load("ModelJoblib")

    data_pred = pd.DataFrame(data = [[city,city_development_index,gender,relevent_experience,enrolled_university,education_level,
    major_discipline,experience,experience,company_size,company_type,last_new_job,training_hours]],
    columns = ['city','city_development_index','gender','relevent_experience','enrolled_university','education_level',
    'major_discipline','experience','experience','company_size','company_type','last_new_job','training_hours'])

    prediksi = model.predict(df_predicts)
    pred = prediksi[0]

    return render_template('result.html', 
        city = city,
        city_development_index= city_development_index,
        gender= gender,
        relevent_experience = relevent_experience,
        enrolled_university = enrolled_university,
        education_level = education_level,
        major_discipline = major_discipline,
        experience = experience,
        company_size = company_size,
        company_type = company_type,
        last_new_job = last_new_job,
        training_hours = training_hours,
        pred = (np.expm1(pred).round(2))
        )

if __name__ == '__main__':
    model = joblib.load("ModelJoblib")
    server.run(debug=True, port=1212)
