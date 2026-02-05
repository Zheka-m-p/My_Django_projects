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


class CreateBotUser(APIView):
    @staticmethod
    def post(request):
        usr_obj: models.BotUserModel = models.BotUserModel.objects.get_or_create(
            chat_id=request.data['chat_id'],
            defaults={
                'first_name': request.data['first_name'],
                'last_name': request.data['last_name'],
                'username': request.data['username'],
            })[0] # Создаем нового пользователя, если еще нет, иначе получаем старого

        usr_obj.save() # обновляем значение поля updated на актуальное время, вызвав сохранение объекта.
        return Response(status=200) # возвращаем ответ со статус-кодом 200:

