from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import SignupForm, LoginForm

# import sending email 
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'No Name')
        email = request.POST.get('email', 'No Email')
        message = request.POST.get('message', 'No Message')
        phone = request.POST.get('phone', 'No Phone')

        send_mail(
            f'Message from: {name}',
            f'Phone: {phone} \n\nMessage: {message}',
            settings.EMAIL_HOST_USER,
            ['karlanthony521@gmail.com'],
            fail_silently=False
        )
    return render(request, 'home.html')

def signup_view(request):   
    if request.method == 'POST':
        form = SignupForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# sending email

# def sending_email(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         message = request.POST['message']
#         send_mail(
#             'Contack Form',
#             message,
#             settings.EMAIL_HOST_USER,
#             [email],
#             fail_silently=False)
#     return render(request, 'index.html')

