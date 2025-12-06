'''
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.

def home(request):
    pro = Product.objects.all()
    if request.method == 'POST':
        proForm = ProductForm(request.POST)
        if proForm.is_valid():
            proForm.save()
            return redirect('/')
    else :
        proForm = ProductForm()
    return render(request,'home/home.html',{
    'pro':pro,'proForm':proForm
    })
'''
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import HttpResponseForbidden

def home(request):
    # --- البحث ---
    query = request.GET.get("q")  # اسم أو سعر
    if query:
        pro = Product.objects.filter(title__icontains=query) | Product.objects.filter(price__icontains=query)
    else:
        pro = Product.objects.all()

    # --- الإضافة ---
    if request.method == 'POST':
        proForm = ProductForm(request.POST)
            #if user_form.is_valid() and profile_form.is_valid():
        if proForm.is_valid():
            product = proForm.save(commit=False)
            product.user = request.user
                #proForm.save()
            product.save()
            return redirect('home')
    else:
        proForm = ProductForm()
    return render(request,'home/home.html',{
        'pro': pro,
        'proForm': proForm
    })

'''

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user   # ربط المنتج بصاحب الحساب
            product.save()
            return redirect("home")
    else:
        form = ProductForm()
    return render(request, "add.html", {"form": form})
'''
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = ProductForm(instance=product)
    return render(request, "home/edit.html", {"form": form})


def delete_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product.delete()
            return redirect("home")
    form = ProductForm(instance=product)
    return render(request,"home/delete.html",{'form':form})
