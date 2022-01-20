from rest_framework import viewsets
from doge.serializers import DogeSerializer
from doge.models import Doge


class dogeViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать щенков на продажу
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Doge.objects.all().order_by('date_modified')
    serializer_class = DogeSerializer  # Сериализатор для модели