from django.shortcuts import render
from .models import Menu
from django.shortcuts import get_object_or_404
from .forms import MenuFilterForm
# Create your views here.
def menu(request):
    menus = Menu.objects.all()
    form = MenuFilterForm(request.GET)
    if form.is_valid():
        burger_type = form.cleaned_data.get('burger_type')
        if burger_type:
            menus = menus.filter(type=burger_type)
    return render(request, 'menu.html', {'menus': menus, 'form': form})