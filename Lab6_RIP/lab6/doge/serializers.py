from doge.models import Doge
from rest_framework import serializers


class DogeSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Doge
        # Поля, которые мы сериализуем
        fields = ["pk", "dog_breed","dog_name", "price", "status", "date_modified"]