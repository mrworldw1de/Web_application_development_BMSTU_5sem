# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    idauthor = models.AutoField(db_column='idAuthor', primary_key=True)  # Field name made lowercase.
    authorname = models.CharField(db_column='Authorname', unique=True, max_length=60)  # Field name made lowercase.
    authorbio = models.CharField(db_column='Authorbio', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'author'


class Book(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    dicription = models.CharField(max_length=255, blank=True, null=True)
    bookauthor = models.ForeignKey(Author, models.DO_NOTHING, db_column='bookauthor', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'book'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Doge(models.Model):
    name = models.CharField(max_length=30)
    dicription = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'doge'


class Kit(models.Model):
    name = models.CharField(max_length=30)
    dicription = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'kit'
