from django.http import HttpResponse
from django.shortcuts import render

def create(request):
    print("Request method is",request.method)
    if request.method=="GET":
        return render(request,'create.html')
    else:
        return HttpResponse("inserted successfully")
