from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("hi...welcome to django class")
def index(request):
    return render(request,'index.html')
