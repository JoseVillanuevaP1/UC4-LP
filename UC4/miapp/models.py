from django.db import models

# Create your models here.
class Course(models.Model):
    idcourse = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True, verbose_name="Codigo")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    hour = models.IntegerField(verbose_name="Horas")
    credits = models.IntegerField(verbose_name="Créditos")
    state = models.BooleanField(default=True, verbose_name="Estado")

    # auto_now_add me permitirá registrar 
    # la fecha cuando cree el registro
    create = models.DateTimeField(auto_now_add=True)
    # auto_now me permitirá registrar 
    # la fecha cuando se modifique el registro
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name