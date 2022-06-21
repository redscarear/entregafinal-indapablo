from cProfile import label
from django.db import models
class Evento(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    code = models.IntegerField()
    description = models.TextField(blank = True, null=True)
    def __str__(self):
        return f'{self.name} evento --'