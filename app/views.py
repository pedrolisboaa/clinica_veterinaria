from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from time import sleep

# FORMULARIOS 
from .forms import EnderecoForm, TutorForm

# MODELS
from .models import Tutor

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

@login_required
def tutor_listar(request):
    
    tutores = Tutor.objects.order_by('-id')
    
    
    contex = {
        'tutores': tutores
    }
    
    return render(request, 'tutor/tutor_listar.html', contex)


@login_required
def tutor_editar(request, id_tutor):
    tutor = Tutor.objects.get(pk=id_tutor)

    if request.method == 'POST':
        form = TutorForm(request.POST, instance=tutor)
        endereco_form = EnderecoForm(request.POST, instance=tutor.endereco)  # Adicione esta linha
        if form.is_valid() and endereco_form.is_valid():
            form.save()
            endereco_form.save()
            messages.success(request, 'Tutor atualizado com sucesso.')
            sleep(1)
            return redirect('tutor_listar')
    else:
        form = TutorForm(instance=tutor)
        endereco_form = EnderecoForm(instance=tutor.endereco)  # Adicione esta linha

    context = {
        'form': form,
        'endereco_form': endereco_form,  # Adicione esta linha
        'tutor': tutor,
    }

    return render(request, 'tutor/tutor_editar.html', context)

@login_required
def tutor_deletar(request, id_tutor):
    tutor = Tutor.objects.get(pk=id_tutor)
    
    if request.method == 'POST':
        tutor.delete()
        return redirect('tutor_listar')
    return render(request, 'tutor/tutor_deletar.html', {'tutor':tutor})