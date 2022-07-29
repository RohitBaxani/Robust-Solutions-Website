import email
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    return render(request,'index.html',context)
    #return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def courses(request):
    return render(request,'courses.html')
    #return HttpResponse("this is courses page")

def contact(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        age=request.POST.get('age')
        location=request.POST.get('location')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(firstname=firstname, lastname=lastname, age=age, location=location, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent!')
    return render(request,'contactus.html')
    #return HttpResponse("this is contact page")