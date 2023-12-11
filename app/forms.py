from django import forms
from .models import Tutor, Endereco


# TUTOR
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'cidade', 'estado', 'complemento',]
        widgets = {
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nome', 'cpf', 'email', 'data_de_nascimento',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'data_de_nascimento': forms.DateInput(attrs={'class': 'form-control','type':'date' ,'placeholder': 'Data denascimento'}),
        }
