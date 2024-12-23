from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def introduction(request):
    return render(request, "introduction.html")

def profile(request):
    return render(request, "profile.html")

def index(request):
    return render(request, "index.html")

def form(request):
    return render(request, "form.html")

def naturopath(request):
    return render(request, "naturopath.html")
