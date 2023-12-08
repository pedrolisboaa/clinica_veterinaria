from django.db import models




# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=150)
    estados = models.CharField(max_length=50)
    complemento = models.CharField(max_length=100)
    


class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    data_de_nascimento = models.DateField(null=False, blank=False)
    data_de_cadastro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nome