from django.db import models


# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=50)
    complemento = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cidade} - {self.complemento}'


class Tutor(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    contato = models.CharField(max_length=11)
    email = models.EmailField(null=False, blank=False, unique=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    data_de_nascimento = models.DateField(null=False, blank=False)
    data_de_cadastro = models.DateField(auto_now_add=True)
    

    
    def __str__(self):
        return self.nome
    
    
class Pet(models.Model):
    ESCOLHA_SEXO = (
        ("M", 'Masculino'),
        ("F", 'Feminino'),
    )
    
    ESPECIE = (
        ("G", 'Gato'),
        ("C", 'Cachorro'),
        ("E", 'Exótico'),
    )
    nome = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=ESCOLHA_SEXO)
    especie = models.CharField(max_length=1, choices=ESPECIE)
    cor = models.CharField(max_length=100, null=False, blank=False)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, default=None)
    