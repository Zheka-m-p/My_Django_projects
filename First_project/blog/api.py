from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers


class GetFilePath(APIView):
    @staticmethod
    def get(request):
        code = request.GET.get('code') # 1. Берём код из запроса (например: ?code=68)
        try:
            file = models.PostFilesModel.objects.get(code=code) # 2. Ищем файл в базе по коду
            file.increment_download_count() # 3. Увеличиваем счётчик скачиваний
            serialized_data = serializers.FileModelSerializer(file) # 4. Превращаем файл в JSON через сериализатор
            return Response(serialized_data.data) # 5. Возвращаем JSON
        except ObjectDoesNotExist:
            return Response(None, status=404) # 6. Если файл не найден — ошибка 404

