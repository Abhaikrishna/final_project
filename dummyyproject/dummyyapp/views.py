from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from .models import member
#Create your views here.

def dummyy(request):
    obj=Place.objects.all()
    mm=member.objects.all()
    return render(request,"index.html",{'result':obj,'result2':mm})

def Form(request):
    return render(request,"Form.html")