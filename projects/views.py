from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Product
from .models import Category
from .models import Ticket
from django.contrib.auth.models import User
# Create your views here.

def index(request,slug=None):
    if slug is not None:
        try:
            product = Product.objects.get(slug=slug)
            print(product)
            return render(request, 'projects/products/slug.html', {"product": product})
        except:
            return render(request, 'projects/404.html')
    else:
        products = Product.objects.all()
        return render(request, 'projects/products/index.html', {"products": products})

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
    return render(request, 'projects/products/create.html', {"categories": categories})

def editProject(request, slug):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        category = Category.objects.get(category_name=request.POST['category'])
        if name == '':
            messages.error(request, 'Please add a title')
            return redirect('editProject')
        else:
            project = Product.objects.filter(slug=slug).update(name=name, product_description=description, slug=slug, category=category)
            messages.success(request, 'Project updated')
            return redirect('index')
    try:
        product = Product.objects.get(slug=slug)
        categories = Category.objects.all()
        return render(request, 'projects/products/edit.html', {"product": product, "categories": categories})
    except:
        return render(request, 'projects/404.html')

def deleteProject(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        product.delete()
        messages.success(request, 'Project deleted')
        return redirect('index')
    except:
        return render(request, 'projects/404.html')

def indexTickets(request, slug=None):
    if slug is not None:
        try:
            ticket = Ticket.objects.get(slug=slug)
            return render(request, 'projects/tickets/slug.html', {"ticket": ticket})
        except:
            return render(request, 'projects/404.html')
    else:
        tickets = Ticket.objects.all()
        return render(request, 'projects/tickets/index.html', {"tickets": tickets})

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

    return render(request, 'projects/tickets/create.html', {"products": products, "users": users})

def editTicket(request, slug):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        product = Product.objects.get(name=request.POST['product'])
        user = User.objects.get(username=request.POST['user'])
        if name == '':
            messages.error(request, 'Please add a title')
            return redirect('editTicket')
        else:
            ticket = Ticket.objects.filter(slug=slug).update(name=name, description=description, slug=slug, product=product, user=user)
            messages.success(request, 'Ticket updated')
            return redirect('index')
    try:
        ticket = Ticket.objects.get(slug=slug)
        products = Product.objects.all()
        users = User.objects.all()
        return render(request, 'projects/tickets/edit.html', {"ticket": ticket, "products": products, "users": users})
    except:
        return render(request, 'projects/404.html')

def deleteTicket(request, slug):
    try:
        ticket = Ticket.objects.get(slug=slug)
        ticket.delete()
        messages.success(request, 'Ticket deleted')
        return redirect('index')
    except:
        return render(request, 'projects/404.html')

def indexCategories(request, slug=None):
    if slug is not None:
        try:
            category = Category.objects.get(slug=slug)
            return render(request, 'projects/categories/slug.html', {"category": category})
        except:
            return render(request, 'projects/404.html')
    else:
        categories = Category.objects.all()
        return render(request, 'projects/categories/index.html', {"categories": categories})

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

    return render(request, 'projects/categories/create.html')

def editCategory(request, slug):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        if name == '':
            messages.error(request, 'Please add a title')
            return redirect('editCategory')
        else:
            category = Category.objects.filter(slug=slug).update(category_name=name, category_description=description)
            messages.success(request, 'Category updated')
            return redirect('index')
    try:
        category = Category.objects.get(slug=slug)
        return render(request, 'projects/categories/edit.html', {"category": category})
    except:
        return render(request, 'projects/404.html')

def deleteCategory(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        category.delete()
        messages.success(request, 'Project deleted')
        return redirect('index')
    except:
        return render(request, 'projects/404.html')