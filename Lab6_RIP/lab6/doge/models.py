from django.db import models


class Doge(models.Model):
    dog_breed = models.CharField(max_length=50, verbose_name="Название породы")
    dog_name = models.CharField(max_length=50, verbose_name="Кличка")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена щенка")
    status = models.BooleanField(verbose_name="Продаётся?")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="Когда последний раз обновлялись данные?")