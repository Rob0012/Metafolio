from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
import requests

def main(request):
    return render(request,"base.html")    

def home(request):
    email_list = User.objects.values_list('email', flat=True)
    
    return render(request, 'main.html', {'email_list': email_list})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user = User.objects.get(username=username)
            
            url_to_scrape = "https://google.com"
            web = requests.get(url_to_scrape)
            if user.email in str(web.content).lower():
                return HttpResponse("<h1>Found in " + url_to_scrape + "</h1>")
            return HttpResponse("<h1>Not Found in " + url_to_scrape + "</h1>")  
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            
            user.phone_number = phone_number
            
            if 'image' in request.FILES:
                user.image = request.FILES['image']

            user.save()

            messages.success(request, 'Account created successfully. Please log in.')

            return redirect('login')  
        
    return render(request, 'signup.html')

