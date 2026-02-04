from django import forms
from .models import Menu

class MenuFilterForm(forms.Form):
    burger_type = forms.ChoiceField(
        choices=[('', 'All Burgers')] + list(Menu.MENU_TYPE_LIST),
        required=False,
        label="Filter by Burger Type"
    )