from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


#LOGIN--------------------------------------------------------------
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')
    
    return render(request, 'index.html')


#HOME_--------------------------------------------------------------
@login_required()
def home(request):
    return render(request, 'home.html')


# ERROS--------------------------------------------------------------
def custom_404(request, exception):
    return render(request, '404.html', status=404)