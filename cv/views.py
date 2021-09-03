from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeview(*args, **kwargs):
    return HttpResponse("<h1> Hello World. THats my fucking website. Its gonna b grand MF......!!! </h1>")