from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

#View a list of database objects
def product_list_view(request):
    queryset = Product.objects.all() #List of objects
    context = {
        'object_list' : queryset  #typical context variable name
    }
    return render(request, 'products/product_list.html', context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id) #list of objects
    context = {
        'object' : obj
    }
    return render(request, 'products/product_detail.html', context)


#Delete and Object
def product_delete_view(request, id):
    obj = Product.objects.get(id=id)
    #POST request is good, not GET  request...DELETE can also be used

    if request.method == 'POST':
        #Confirming delete
        obj.delete()
        return redirect('../')
        
    context = {
        'object' : obj
    }
    return render(request, 'products/product_delete.html', context)









#Dynamic lookup
"""def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context = {
        'object' : obj
        
    }
    return render(request, 'products/product_detail.html', context)
"""


"""try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404"""
#Dynamic url routing allows you to request db objects using their id's
#id=my_id.......(request, my_id)

#To handle a missing object, import get_object_or_404. It's also good for error handling
#It can also be placed in a try block


"""def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            #now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    
    context = {
        'form' : my_form
    }
    return render(request, 'products/product_create.html', context)
"""

"""def product_create_view(request):
    #print(request.GET)
    #print(request.POST)
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        print(my_new_title)
    context = {}
    return render(request, "products/product_create.html", context)
"""


#Render Initial data and change object in database
"""def product_create_view(request):
    initial_data = {
        'title' : 'My awesome title'
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj, initial=initial_data)
    if form.is_valid:
        form.save()
    context = {
        'form' : form
    }
    return render(request, 'products/product_create.html', context)
"""