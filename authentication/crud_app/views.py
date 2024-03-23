from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_url')
def add_product(request):
    template_name = 'crud_app/add.html'
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_product(request):
    template_name = 'crud_app/show.html'
    orders = Product.objects.all()
    context = {'orders': orders}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def update_product(request, pk):
    template_name = 'crud_app/add.html'
    obj = Product.objects.get(id=pk)
    form = ProductForm(instance=obj)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def cancel_product(request, pk):
    obj = Product.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    return render(request, 'crud_app/confirm.html')