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
    items=json.loads(prepare_data())
    context = {'HeadText':'Stats by Date',
              'baseUrl':baseUrl, 'items':items}

    #HeadText='Stats by Date'
    return HttpResponse(template.render(context, request));


def prepare_data():
    timelog=open('updatedDate.log','r')
    lasttime=timelog.read()
    if lasttime > '':
        lasttime=float(lasttime)
    else:
        lasttime=0.0
    timelog.close()
    curtime=time.time()
    if (curtime-lasttime > 0):
        print("Fetching Updated JSON for INDIA Data")
        timelog2=open('updatedDate.log','w')
        response = requests.get("https://api.covid19india.org/data.json")
        print(response.status_code)
        if response.status_code == requests.codes.ok:
            res=response.json()
            F1=open("./static/js/result.js",'wb')
            F1.write(response.content)
            F1.close()
            timelog2.write(str(curtime))
        timelog2.close()
        return response.content

def ind_states(request):
    baseUrl=request.build_absolute_uri()[:-1*len('/ind_state')]
    template = loader.get_template('./indbyStates.html')
    items=json.loads(prepare_data())
    context = {'HeadText':'Stats by State',
    'baseUrl':baseUrl, 'items':items}
    print(items)
    return HttpResponse(template.render(context, request));

def ind_test(request):
    baseUrl=request.build_absolute_uri()[:-1*len('/ind_test')]
    template = loader.get_template('./indTest.html')
    context = {'HeadText':'Test Status by Date',
    'baseUrl':baseUrl}
    prepare_data()
    return HttpResponse(template.render(context, request));


