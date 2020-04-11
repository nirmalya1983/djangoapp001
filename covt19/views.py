from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
import json
import time


def index(request):
    baseUrl=request.build_absolute_uri()[:-1]
    template = loader.get_template('./index.html')
    prepare_data()
    context = {'HeadText':'Stats by Date',
              'baseUrl':baseUrl}
    #HeadText='Stats by Date'
    return HttpResponse(template.render(context, request));


def prepare_data():
    with open('updatedDate.log','r+') as timelog:
        lasttime=timelog.read()
        if lasttime > '':
            lasttime=float(lasttime)
        else:
            lasttime=0.0
        curtime=time.time()
        if (curtime-lasttime > 3600):
            print("Fetching Updated JSON for INDIA Data")
            response = requests.get("https://api.covid19india.org/data.json")
            print(response.status_code)
            if response.status_code == requests.codes.ok:
                res=response.json()
                F1=open("./static/js/result.js",'wb')
                F1.write(response.content)
                F1.close()
                timelog.write(str(curtime))

def ind_states(request):
    baseUrl=request.build_absolute_uri()[:-1*len('/ind_state')]
    template = loader.get_template('./indbyStates.html')
    context = {'HeadText':'Stats by State',
    'baseUrl':baseUrl}
    return HttpResponse(template.render(context, request));


