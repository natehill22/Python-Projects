from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    products = ["Cherries", "Apples", "Orange", "Strawberries", "Pears", "Watermelons"]
    user = request.user
    context = {
        'products': products,
    }
    return render(request, "home.html", context)