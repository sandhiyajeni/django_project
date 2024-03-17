from django.http import HttpResponse
from django.shortcuts import render

def create(request):
    print("Request method is",request.method)
    if request.method=="GET":
        return render(request,'create.html')
    else:
        n=request.POST['uname']
        e=request.POST['uemail']
        m=request.POST['umbno']
        msg=request.POST['msg']
        print("Name is",n)
        print("email is",e)
        print("mobile no is",m)
        print("message is",msg)
        return HttpResponse("inserted successfully")
