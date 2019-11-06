from django.db import models

class registroC(models.Model):
    Nombre = models.CharField(max_length=25, help_text="Ingresa tu nombre")
    Apellido = models.CharField(max_length=25, help_text="ingresa tu apellido")
    colonia = models.CharField(max_length=45, help_text="ingresa tu colona")
    E_mail = models.EmailField()
    
