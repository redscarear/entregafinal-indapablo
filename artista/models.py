from django.db import models
class Artista(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    instrument = models.CharField(max_length=40)
    cuil = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f'Nombre del Artista: {self.name} {self.last_name} -- '