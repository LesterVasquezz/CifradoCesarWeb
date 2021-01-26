from django.db import models

# Create your models here.
class encriptarMod (models.Model):
    palabra=models.CharField(max_length=200)
    llave=models.PositiveIntegerField()

    def __str__(self):
        return self.palabra

class descriptarMod (models.Model):
    mensaje=models.CharField(max_length=200)
    llave=models.PositiveIntegerField()
    
    def __str__(self):
        return self.mensaje