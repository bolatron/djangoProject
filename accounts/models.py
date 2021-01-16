from django.db import models

# Create your models here.

class Account(models.Model):

    # Campos obrigatórios

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    birth_date = models.DateField(null=True)
    email = models.EmailField()
    
    # Campos complementares e não obrigatórios

    nickname = models.CharField(max_length=255)
    observations = models.TextField()

    def __str__(self):
        return f'Perfil do { self.first_name } { self.last_name }'