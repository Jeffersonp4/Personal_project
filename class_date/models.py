from django.db import models

# Create your models here.

class conexs_pool(models.Model):
    ip = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    db_type = models.CharField(max_length=100)
    Active = models.BooleanField()

    def __str__(self):
        return f'Conexion {self.id}: {self.ip} {self.user} {self.pwd} {self.db_type} {self.Active}'

