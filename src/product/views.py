from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawProduction
# Create your views here.

def product_create_view(request):
    inital_data = {
            'title': "This is my awesome title"
    }

    form = ProductForm(request.POST or None )

    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        "form": form
    }
    return render(request, "products/form_create.html", context)
def product_detail_view(request, getID):
    obj = get_object_or_404(Product, id=getID)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


# def render_initial_data(request):
#     inital_data = {
#         'title': "This is my awesome title"
#     }
#     form = RawProduction(request.POST or None, initial = inital_data)
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)