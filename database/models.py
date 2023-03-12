from django.db import models

# Create your models here.
class PrimaryDate(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    disease = models.CharField(max_length=40)

    

