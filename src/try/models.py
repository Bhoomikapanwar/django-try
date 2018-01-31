from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=120)
    use = models.CharField(max_length=120, null = True, blank = True)
