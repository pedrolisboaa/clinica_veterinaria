from django import forms
from .models import Tutor, Endereco


# TUTOR
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['cep', 'cidade', 'estado', 'complemento',]


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['nome', 'cpf', 'email', 'data_de_nascimento',]

