from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    codigo_isbn = models.CharField(max_length=200, unique=True)
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='articulos/', null=True, blank=True)
    precio = models.PositiveBigIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_code_name()

    def get_code_name(self):
        return f" ISBN: {self.codigo_isbn} - {self.nombre}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    orden = models.CharField(max_length=200)
    correo = models.EmailField()
    motivo = models.TextField()

    def __str__(self):
        return f"{self.nombre}{self.apellido}{self.orden}"

class User(AbstractUser):
    es_administrador = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

User = get_user_model()
