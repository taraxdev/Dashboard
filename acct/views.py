from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,"acct/index.html")

def product(request):
    return render(request,"acct/products.html")

def dashboard(request):
    return render(request,"acct/dashboard.html")

def customer(request):
    return render(request,"acct/customer.html")
