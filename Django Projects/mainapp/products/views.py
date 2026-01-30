from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm
from .models import Product

def admin_console(request):
    products = Product.objects.all() #Gets all data from the Products table
    return render(request, 'products/products_page.html', {'products': products}) #Shows all Product data on the products page


def details(request, pk): #Defines the function and the parameters used (request is part of the HTTPrequest)
    pk = int(pk) #Setting the pk variable to an integer value of the primary key, captured from the URL
    item = get_object_or_404(Product, pk=pk) #Setting the item variable to the value of the dB's Product model using the particular record taken from the URL before, if errors, show a 404
    form = ProductForm(data=request.POST or None, instance=item) #Setting the form variable to be the Product-based ModelForm using POST data (or none at all) pre-filled with the specific item/Product's data
    if request.method == 'POST': #If the request.method attribute (which is a standard and auto-populated part of the HTTPrequest object) contains POST (that information was posted/shown to us)
        if form.is_valid(): #If data on form is correct and unaltered,
            form2 = form.save(commit=False) #Takes data from the form, but does not save it to the database and gives it the value of the form2 variable
            form2.save() #Commits the data to the database
            return redirect('admin_console') #Goes back to the admin console
        else:
            print(form.errors) #Otherwise, print the errors seen on the form
    else:
        return render(request, 'products/present_product.html', {'form': form}) #Returns the request on the present products page with the Product form information


def delete(request, pk): #Defines the function and the parameters used (request is part of the HTTPrequest)
    pk = int(pk) #Setting the pk variable to an integer value of the primary key, captured from the URL
    item = get_object_or_404(Product, pk=pk) #Setting the item variable to the value of the dB's Product model using the particular record taken from the URL before, if errors, show a 404
    if request.method =='POST': #If the request.method attribute (which is a standard and auto-populated part of the HTTPrequest object) contains POST (that information was posted/shown to us)
        item.delete() #Delete the item--the Product model for that specific record
        return redirect('admin_console') #Brings the user back to the admin console
    context = {"item": item,} #Otherwise, turn the "item" variable into a dictionary (required by render) and assign it to the context variable
    return render(request, "products/confirmDelete.html", context) #Returns the request on the confirmDelete page with the dictionary variable information above


def confirmed(request):
    if request.method =='POST': #If the request.method attribute (which is a standard and auto-populated part of the HTTPrequest object) contains POST (that information was posted/shown to us)
        form = ProductForm(request.POST or None) #Create a form instance and bind Product data to it
        if form.is_valid(): #If data on form is correct and unaltered,
            form.delete() #Delete the record from the database
            return redirect('admin_console') #Go back to admin page
    else:
        return redirect('admin_console') #Otherwise, go back to admin page


def createRecord(request):
    form = ProductForm(request.POST or None) #Create a form instance and bind Product data to it
    if form.is_valid(): #If data on form is correct and unaltered,
        form.save() #Commits the data to the database
        return redirect('admin_console') #Go back to the admin console
    else:
        print(form.errors) #Otherwise, show the errors
        form = ProductForm() #Assign the empty Product data on the Model form to the form variable
    context = {"form": form,} #Turn the "form" variable into a dictionary (required by render) and assign it to the context variable
    return render(request, 'products/createRecord.html', context) #Returns the request on the createRecord page with the dictionary variable information above