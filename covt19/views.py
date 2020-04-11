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
    context = {'HeadText':'Stats by Date'}
    #HeadText='Stats by Date'
    return HttpResponse(template.render(context, request));


def prepare_data():
    response = requests.get("https://api.covid19india.org/data.json")
    print(response.status_code)
    if response.status_code == requests.codes.ok:
        res=response.json()
        F1=open("./static/js/result.js",'wb')
        F1.write(response.content)
        F1.close()

def ind_states(request):
    template = loader.get_template('./indbyStates.html')
    context = {'HeadText':'Stats by State'}
    return HttpResponse(template.render(context, request));


