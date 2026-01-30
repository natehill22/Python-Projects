from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_console', views.admin_console, name='admin_console'), #URL path to the admin page
    path('<int:pk>/details/', views.details, name='details'), #URL path for Product details page
    path('<int:pk>/delete/', views.delete, name='delete'), #URL path for Product delete page
    path('confirmdelete/', views.confirmed, name='confirmed'),  # URL path for Product delete confirmation page
    path('createRecord/', views.createRecord, name='createRecord'),  # URL path for Product creation page

]