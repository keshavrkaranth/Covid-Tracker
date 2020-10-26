from django.shortcuts import render
import requests
from django.contrib import messages


# Create your views here.
def Homepage(request):
    url = "https://api.covid19api.com/summary"
    data = requests.get(url).json()
    global_data = data['Global']
    country = data['Countries']
    return render(request,'covid-body.html',{'global':global_data,'country':country})
