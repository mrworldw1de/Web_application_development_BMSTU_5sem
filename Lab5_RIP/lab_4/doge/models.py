from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30)
    dicription  = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'books'

class Doge(models.Model):
    name = models.CharField(max_length=30)
    dicription  = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'doge'

class Kit(models.Model):
    name = models.CharField(max_length=30)
    dicription  = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kit'