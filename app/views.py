from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# FORMULARIOS 
from .forms import EnderecoForm, TutorForm

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


#TUTOR
@login_required
def tutor_cadastrar(request):
    if request.method == 'POST':
        endereco_form = EnderecoForm(request.POST)
        tutor_form = TutorForm(request.POST)

        if endereco_form.is_valid() and tutor_form.is_valid():
            endereco = endereco_form.save()
            tutor = tutor_form.save(commit=False)
            tutor.endereco = endereco
            tutor.save()
            return redirect('home')
    else:
        endereco_form = EnderecoForm()
        tutor_form = TutorForm()
    
    context = {
        'endereco_form': endereco_form,
        'tutor_form': tutor_form,
    }

    return render(request, 'tutor/tutor_cadastrar.html', context)