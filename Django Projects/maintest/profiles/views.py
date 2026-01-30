from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile #Import Profile module

def user_profiles(request):
    #Retrieve all profiles from the database
    profiles = Profile.objects.all()
    #Pass profiles list into the template context
    context = {'profiles': profiles}
    return render(request, 'home.html', context)


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        return render(request, 'present_profile.html', {'form': form})


def delete(request, pk): #Defines the function and the parameters used (request is part of the HTTPrequest)
    pk = int(pk) #Setting the pk variable to an integer value of the primary key, captured from the URL
    item = get_object_or_404(Profile, pk=pk) #Setting the item variable to the value of the dB's Profile model using the particular record taken from the URL before, if errors, show a 404
    if request.method =='POST': #If the request.method attribute (which is a standard and auto-populated part of the HTTPrequest object) contains POST (that information was posted/shown to us)
        item.delete() #Delete the item--the Profile model for that specific record
        return redirect('/') #Brings the user back to the home
    context = {"item": item,} #Otherwise, turn the "item" variable into a dictionary (required by render) and assign it to the context variable
    return render(request, "confirmDelete.html", context) #Returns the request on the confirmDelete page with the dictionary variable information above


def confirmDel(request):
    if request.method =='POST': #If the request.method attribute (which is a standard and auto-populated part of the HTTPrequest object) contains POST (that information was posted/shown to us)
        form = ProfileForm(request.POST or None) #Create a form instance and bind Profile data to it
        if form.is_valid(): #If data on form is correct and unaltered,
            form.delete() #Delete the record from the database
            return redirect('/') #Go back to home page
    else:
        return redirect('/') #Otherwise, go back to home page

def createRecord(request):
    form = ProfileForm(request.POST or None) #Create a form instance and bind Product data to it
    if form.is_valid(): #If data on form is correct and unaltered,
        form.save() #Commits the data to the database
        return redirect('home') #Go back to the admin console
    else:
        print(form.errors) #Otherwise, show the errors
        form = ProfileForm() #Assign the empty Product data on the Model form to the form variable
    context = {"form": form,} #Turn the "form" variable into a dictionary (required by render) and assign it to the context variable
    return render(request, 'createRecord.html', context) #Returns the request on the createRecord page with the dictionary variable information above