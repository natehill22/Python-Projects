from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/details/', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('confirmDelete/', views.confirmDel, name='confirmDel'),  # URL path for Profile delete confirmation page
    path('createRecord/', views.createRecord, name='createRecord'),  # URL path for Profile creation page

]