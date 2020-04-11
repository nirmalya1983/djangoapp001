from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
import json


def index(request):
    template = loader.get_template('./index.html')
    prepare_data()
    context = {'latest_question_list': "abcd"}
    return HttpResponse(template.render(context, request));


def prepare_data():
    response = requests.get("https://api.covid19india.org/data.json")
    print(response.status_code)
    if response.status_code == requests.codes.ok:
        res=response.json()
        F1=open("./static/js/result.js",'wb')
        F1.write(response.content)
        F1.close()

