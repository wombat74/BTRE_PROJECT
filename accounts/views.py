from django.shortcuts import redirect, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User # this is used to check usernames

def register(request):
    if request.method == 'POST':
        # Get form values (these are coming from the form as POST request)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            if User.objects.filter(username=username).exists(): # checking the db to see if the "username" value exists
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists(): # checking the db to see if the "email" value exists
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # Below is an alternate way to do this using: from django.contrib import auth
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in!')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Check username
        pass
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

