from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello, this is the index page of myapp.")

def maps(request):
  return HttpResponse("This is the about page of myapp.")
