from django.db import models

class Cerveja(models.Model):
	nome = models.CharField(max_length=100, blank=True, verbose_name='Nome')
	preco = models.DecimalField() 
