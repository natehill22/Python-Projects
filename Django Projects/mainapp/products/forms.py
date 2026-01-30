from django.forms import ModelForm
from .models import Product

#Combines the built-in ModelForm structure with the full Products database table
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'