from django.db import models

# Create your models here.
class Model(models.Model):
    name        = models.CharField(max_length=120)
    use         = models.CharField(max_length=120, null = True, blank = True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateField(auto_now= True)
