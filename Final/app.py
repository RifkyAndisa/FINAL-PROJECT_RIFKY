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
        #Region
        major = input["MajorD"]
        strMajor = ""
        if major == "stem":
            stem = 1
            bd = 0
            arts = 0
            humanities = 0
            nm = 0
            oth = 0 
            strMajor = "STEM"
        if major == "bd":
            stem = 0
            bd = 1
            arts = 0
            humanities = 0
            nm = 0
            oth = 0 
            strRegion = "Business Degre"
        if major == "arts":
            stem = 10
            bd = 0
            arts = 1
            humanities = 0
            nm = 0
            oth = 0 
            strRegion = "arts"
        if major == "humanities":
            stem = 0
            bd = 0
            arts = 0
            humanities = 1
            nm = 0
            oth = 0 
            strRegion = "humanities"
        if major == "nm":
            stem = 0
            bd = 0
            arts = 0
            humanities = 0
            nm = 1
            oth = 0 
            strRegion = "No Major"
        if major == "oth":
            stem = 0
            bd = 0
            arts = 0
            humanities = 0
            nm = 0
            oth = 1 
            strRegion = "Other Major"
        #Gender
        gender = input["gender"]
        strGender = ""
        if gender == "m":
            mal = 1
            fem = 0
            strGender = "Male"
        if gender == "f":
            mal = 0
            fem = 1
            strGender = "Female"
        #Relevant Experience
        relevant = input["relevant"]
        strRelevant = ""
        if relevant == "y":
            rl = 1
            strRelevant = "Yes"
        else:
            rl = 0
            strRelevant = "No"
        #Enrolled University
        enrolled = input["enrolled"]
        strEnroll = ""
        if enrolled == "y":
            enr = 1
            strEnroll = "Yes"
        else:
            enr = 0
            strEnroll = "No"
        # Educational 
        educational = input["educational"]
        streEdu = ""
        if enrolled == "ps":
            ps = 1
            phd = 0
            hc = 0
            ms = 0
            gr = 0
            strEdu = "Primary School"
        if enrolled == "phd":
            ps = 0
            phd = 1
            hc = 0
            ms = 0
            gr = 0
            strEdu = "Phd"
        if enrolled == "hc":
            ps = 0
            phd = 0
            hc = 1
            ms = 0
            gr = 0
            strEdu = "High School"
        if enrolled == "ms":
            ps = 0
            phd = 0
            hc = 0
            ms = 1
            gr = 0
            strEdu = "Master"
        if enrolled == "gr":
            ps = 0
            phd = 0
            hc = 0
            ms = 0
            gr = 1
            strEdu = "Graduate"
        # Commpany
        commpany = input["commpany"]
        streCom = ""
        if commpany == "pvt":
            pvt = 1
            FS = 0
            ES = 0
            otht = 0
            ps = 0
            ngo = 0
            strEdu = "Pvt Ltd"
        if commpany == "FS":
            pvt = 0
            FS = 1
            ES = 0
            otht = 0
            ps = 0
            ngo = 0
            strEdu = "Funded Start Up"
        if commpany == "ES":
            pvt = 0
            FS = 0
            ES = 1
            otht = 0
            ps = 0
            ngo = 0
            strEdu = "Early STage Start Up"
        if commpany == "otht":
            pvt = 0
            FS = 0
            ES = 0
            otht = 1
            ps = 0
            ngo = 0
            strEdu = "Other Type"
        if commpany == "ps":
            pvt = 0
            FS = 0
            ES = 0
            otht = 0
            ps = 1
            ngo = 0
            strEdu = "Public Sector"
        if commpany == "ngo":
            pvt = 0
            FS = 0
            ES = 0
            otht = 0
            ps = 0
            ngo = 1
            strEdu = "NGO"
        # City Development Index
        city = int(input["city"])
        # Job
        job = int(input["job"])
        # Experience
        experience = int(input["experience"])
        # Training
        training = int(input["training"])
        # Result
        # data yang di masukan harus urut sesuai dataset dummy
        datainput = [[major, gender, relevant, enrolled, educational, commpany, city, job, experience, training]]
        pred_proba = model.predict_proba(datainput)[0]
        if pred_proba == 0:
            # pred = 0
            prbb = round((pred_proba[0]*100), 1)
            rslt = "Not Looking For Job Change"
        else:
            # pred = 1
            prbb = round((pred_proba[1]*100), 1)
            rslt = "Looking for job Change"
        return render_template(
            "result.html", major= strMajor, gender= strGender,
            relevant= strRelevant, enrolled= strEnroll, company= streCom, city= city,
            job = job, experience = experience, training = training)

if __name__ == '__main__':
    model = joblib.load("ModelJoblib")
    server.run(debug=True, port=1212)