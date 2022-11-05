from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Product
from .models import Category
from .models import Ticket
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'projects/all.html')

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        slug = request.POST['slug']
        category = Category.objects.get(category_name=request.POST['category'])
        product_image = request.FILES['product_image']
        if name == '':
            messages.error(request, 'Please add a title')
            return redirect('create')
        else:
            project = Product.objects.create(name=name, product_description=description, slug=slug, category=category, product_image=product_image)
            project.save()
            messages.success(request, 'Project created')
            return redirect('index')

    categories = Category.objects.all()
    return render(request, 'projects/create.html', {"categories": categories})

def createCategory(request):
    if request.method == 'POST':
        category_name = request.POST['category_name']
        slug = request.POST['slug']
        category_description = request.POST['category_description']
        category_image = request.FILES['category_image']
        if category_name == '':
            messages.error(request, 'Please add a title')
            return redirect('createCategory')
        else:
            x = Category.objects.create(category_name=category_name, slug=slug, category_description=category_description, category_image=category_image)
            x.save()
            messages.success(request, 'Category created')
            return redirect('index')

    return render(request, 'projects/createCategory.html')

def createTicket(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        slug = request.POST['slug']
        product = Product.objects.get(name=request.POST['product'])
        user = User.objects.get(username=request.POST['user'])
        if name == '':
            messages.error(request, 'Please add a title')
            return redirect('createTicket')
        else:
            x = Ticket.objects.create(name=name, description=description, slug=slug, product=product, user=user)
            x.save()
            messages.success(request, 'Ticket created')
            return redirect('index')
    products = Product.objects.all()
    users = User.objects.all()

    return render(request, 'projects/createTicket.html', {"products": products, "users": users})


