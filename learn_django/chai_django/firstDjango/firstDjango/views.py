from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, Welcome to home page")
    return render(request, "website/home.html")

def about(request):
    # return HttpResponse("hello, welcome to About page")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello, welcome to conatact page")
    return render(request, 'website/contact.html')

def services(request):
    return render(request, 'website/services.html')
