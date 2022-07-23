from django.shortcuts import render,HttpResponse

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
    return render(request,'contactus.html')
    #return HttpResponse("this is contact page")