from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>WELCOME TO KAKACREATES</h1>")
def about(request):
    return HttpResponse("<h1>ABOUT PAGE</h1>")
def contact(request):
    return HttpResponse("<h1>CONTACT PAGE</h1>")