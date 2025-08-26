from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import PasswordReset
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        messages.error(request, 'Invalid username or password')
        return redirect('login')
    return render(request, 'login.html')    


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
    logout(request)
    messages.success(request, 'Logout successful. Login again')
    return redirect('login')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})
            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'
            email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'

            email_message = EmailMessage(
                'Reset your password', # email subject
                email_body,
                settings.EMAIL_HOST_USER, # email sender
                [email] # email  receiver 
            )

            email_message.fail_silently = True
            email_message.send()
            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f"No user with {email} found")
            return redirect('forgot-password')
    return render(request, 'forgot_password.html')


def passwordResetSent(request, reset_id):
    return render(request, 'password_reset_sent.html')


def resetPassword(request, reset_id):
    return render(request, 'reset_password.html')