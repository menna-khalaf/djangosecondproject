from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.urls import reverse

def product_list(request, category_slug=None):
    categories = Category.objects.filter(is_deleted=False)
    products = Product.objects.filter(is_deleted=False)
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug, is_deleted=False)
        products = products.filter(category=category)
    return render(request, 'store/product_list.html', {
        'categories': categories,
        'products': products,
        'category': category,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_deleted=False)
    return render(request, 'store/product_detail.html', {'product': product})

def product_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image_url = request.POST.get('image_url')
        sku = request.POST.get('sku')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=category_id, is_deleted=False)

        Product.objects.create(
            name=name,
            slug=slug or None,
            description=description,
            price=price,
            stock=stock,
            image_url=image_url,
            sku=sku,
            category=category
        )
        return redirect('store:product_list')

    categories = Category.objects.filter(is_deleted=False)
    return render(request, 'store/product_form.html', {'categories': categories})

def product_edit(request, slug):
    product = get_object_or_404(Product, slug=slug, is_deleted=False)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.slug = request.POST.get('slug') or slugify(product.name)
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.image_url = request.POST.get('image_url')
        product.sku = request.POST.get('sku')
        category_id = request.POST.get('category')
        product.category = get_object_or_404(Category, id=category_id, is_deleted=False)
        product.save()
        return redirect('store:product_list')

    categories = Category.objects.filter(is_deleted=False)
    return render(request, 'store/product_form.html', {
        'product': product,
        'categories': categories
    })

def product_soft_delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.soft_delete()
    return redirect('store:product_list')

def product_hard_delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.delete()
    return redirect('store:product_list')

def category_list(request):
    categories = Category.objects.filter(is_deleted=False)
    return render(request, 'store/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug, is_deleted=False)
    return render(request, 'store/category_detail.html', {'category': category})

def category_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')

        Category.objects.create(
            name=name,
            slug=slug or None,
            description=description
        )
        return redirect('store:category_list')

    return render(request, 'store/category_form.html')

def category_edit(request, slug):
    category = get_object_or_404(Category, slug=slug, is_deleted=False)
    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.slug = request.POST.get('slug') or slugify(category.name)
        category.description = request.POST.get('description')
        category.save()
        return redirect('store:category_list')

    return render(request, 'store/category_form.html', {'category': category})

def category_soft_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category.soft_delete()
    return redirect('store:category_list')

def category_hard_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category.delete()
    return redirect('store:category_list')
