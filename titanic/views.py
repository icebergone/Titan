from django.shortcuts import render
from . import ML_predict

def home(request):
    return render(request, 'index.html')

def result(request):

    pclass = int(request.GET["pclass"])
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    fare = int(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])
    prediction = ML_predict.prediction_model(pclass,sex,age,sibsp,fare,embarked,title)
    return render(request, 'result.html', {'prediction':prediction})
