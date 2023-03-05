from django.db import models

class Menu(models.Model):
    name = models.CharField(verbose_name='nomi', max_length=250)

    def __str__(self):
        return self.name