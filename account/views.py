from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That email is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=username).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')

    return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

    return redirect('index')

def profile(request):
    return render(request, 'accounts/index.html')

def editProfile(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        if username == '':
            messages.error(request, 'Please add a title')
            return redirect('editProfile')
        else:
            user = User.objects.filter(username=username).update(username=username, email=email, first_name=firstname, last_name=lastname)
            messages.success(request, 'User updated')
            return redirect('index')

    return render(request, 'accounts/edit.html')