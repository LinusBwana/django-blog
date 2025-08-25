from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def loginView(request):
    pass        

def registerView(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name').capitalize()
        last_name = request.POST.get('last_name').capitalize()
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_data_has_error = False
    
        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, 'Username already exists')

        if User.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, 'Email already exists')

        if len (password) < 8:
            user_data_has_error = True
            messages.error(request, 'Password must be more than 8 characters')

        if (password != confirm_password):
            user_data_has_error = True
            messages.error(request, 'Passwords do not match')

        if user_data_has_error == False:
            new_user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = password,
            )
            messages.success(request, 'Account created. Login now')
            return redirect('login')
        return render(request, 'register.html', {
                'first_name': first_name,
                'last_name': last_name,
                'username': username,
                'email': email,
                })
    return render(request, 'register.html')


def logoutView(request):
    pass
