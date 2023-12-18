from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def hello(request):
    
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='noida'
        
        
    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b3bfb53aeaa5424e50a1c5d8dba0375b'
    PARAMS={'units':'metric'}
    
    try:
        
      data=requests.get(url,PARAMS).json()
    
      description=data['weather'][0]['description']
      icon=data['weather'][0]['icon']
      temp=data['main']['temp']
    
      day=datetime.date.today()
    
    
    
      return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day, 'city':city,'exception_occured':False})
    
    except:
        exception_occured=True
        messages.error(request,'entered data is not avalaibale on app')
        day=datetime.date.today()
        return render(request,'weatherapp/index.html',{'description':'clear sky','icon':'01d','temp':25,'day':day, 'city':'indore','exception_occured':True})
    