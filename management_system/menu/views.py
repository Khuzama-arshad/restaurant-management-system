from django.shortcuts import render
from .models import Menu
from django.shortcuts import get_object_or_404
# Create your views here.
def menu(request):
    menus = Menu.objects.all()
    return render(request, 'menu.html', {'menus': menus})