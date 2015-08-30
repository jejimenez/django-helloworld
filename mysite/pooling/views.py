from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json

# Create your views here.
def save(request):
    'Save waypoints'
    print('::::::::::::')
    print(request.POST)
    return HttpResponse(json.dumps(dict(isOk=1)))