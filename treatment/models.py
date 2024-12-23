from django.db import models

# Create your models here.

class User(models.Model):
    
    name = models.CharField(max_length=50, null = True, blank = True)
    age = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return 
    
