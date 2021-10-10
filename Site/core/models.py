
from django.db import models
from cloudinary.models import CloudinaryField


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField(max_length=1250)
    image = CloudinaryField(blank=True)
    image_1 = CloudinaryField(blank=True)
    image_2 = CloudinaryField(blank=True)
    image_3 = CloudinaryField(blank=True)
    image_4 = CloudinaryField(blank=True)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome



class Cliente(models.Model):

    Sexo = (
        (u'Masculino', u'Masculino'),
        (u'Feminino', u'Feminino'),
    )

    nome = models.CharField(max_length=100)
    usuario = models.CharField(max_length=18)
    senha = models.CharField(max_length=15)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    data_de_nascimento = models.DateField()
    sexo = models.CharField(max_length=9, choices=Sexo)

    def __str__(self):
        return self.nome
