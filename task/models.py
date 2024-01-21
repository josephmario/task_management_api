from django.db import models

# Create your models here.

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    status = models.IntegerField() 
    def __str__(self):
        return self.description