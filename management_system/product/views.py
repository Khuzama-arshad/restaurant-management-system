from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from .forms import ProductFilterForm
# Create your views here.
def product(request):
    products = Product.objects.all()
    form = ProductFilterForm(request.GET)
    if form.is_valid():
        burger_type = form.cleaned_data.get('burger_type')
        if burger_type:
            products = products.filter(type=burger_type)
    return render(request, 'product.html', {'products': products, 'form': form})