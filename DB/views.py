from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse


def index(request):
  return HttpResponse("Hello, this is the index page of myapp.")

def maps(request):
  return HttpResponse("This is the about page of myapp.")
>>>>>>> 2a6cb2766cf213d452a569e2c1f63982f1aaaec0
