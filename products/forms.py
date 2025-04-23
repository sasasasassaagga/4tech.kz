from django import forms
from .models import *
from .models import Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'rating', 'category', 'thumbnail']



class ProductSearchForm(forms.Form):
    search = forms.CharField(
        label='Name',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search by name'})
    )
    min_price = forms.DecimalField(
        label='Min. Price',
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'From'})
    )
    max_price = forms.DecimalField(
        label='Max. Price',
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'To'})
    )
    min_rating = forms.FloatField(
        label='Min. Rating',
        required=False,
        min_value=0,
        max_value=5,
        widget=forms.NumberInput(attrs={'placeholder': 'From', 'step': '0.1'})
    )
    categories = forms.ModelMultipleChoiceField(
        label='Category',
        required=False,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )