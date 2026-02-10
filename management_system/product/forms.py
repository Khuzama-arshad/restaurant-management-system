from django import forms
from .models import Product

class ProductFilterForm(forms.Form):
    burger_type = forms.ChoiceField(
        choices=[('', 'All Burgers')] + list(Product.PRODUCT_TYPE_LIST),
        required=False,
        label="Filter by Burger Type"
    )