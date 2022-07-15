from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework import status


def send_message_form(request):
    if request.method == 'POST':
        try:
            data = request.POST
            # Добавить "Сохранение сообщений"
            return JsonResponse({'status': 'OK'}, status=status.HTTP_200_OK)
        except:
            return JsonResponse({'status': 'ERROR'}, status=status.HTTP_400_BAD_REQUEST)
