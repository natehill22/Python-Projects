from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from profiles.models import Profile

def home(request):
    names = Profile.objects.all() #Retrieve all profiles from the database
    context = { #Pass profiles list into the template context
        'names': names,
    }

    return render(request, 'home.html', context)
