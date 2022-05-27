from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Product, Category, Comment
from .forms import ProductForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def products_view(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categories = Category.objects.all()
    products = Product.objects.filter(Q
                                      (category__name__icontains=q) |
                                      Q(title__icontains=q))
    products_count = products.count()
    context = {'products': products, 'categories': categories, 'products_count': products_count}
    return render(request, 'products/list_of_products.html', context)

def product_detail_view(request, pk):
    product = Product.objects.get(id = pk)
    product_comments = product.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            product=product,
            body=request.POST.get('body')
        )
        return redirect('product-detail', pk=product.id)
    context = {'product': product, 'product_comments': product_comments}
    return render(request, 'products/detail_product.html', context)

@staff_member_required(login_url='/login')
def create_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form': form}
    return render(request, 'products/product_from.html', context)

@staff_member_required(login_url='/login')
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form': form}
    return render(request, 'products/product_from.html', context)

@staff_member_required(login_url='/login')
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'products/delete.html', {'obj': product})

@login_required(login_url='login')
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse("hola hola!")

    if request.method == 'POST':
        comment.delete()
        return redirect('products')

    return render(request, 'products/delete.html', {'obj': comment})