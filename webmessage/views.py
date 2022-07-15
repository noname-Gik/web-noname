from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework import status
from rest_framework.views import APIView

from webmessage.models import MessageMode
from rest_framework.response import Response

from webmessage.serializer import MessageModeSerializer


class MessageList(APIView):
    def get(self, request, format=None):
        snippets = MessageMode.objects.all()
        serializer = MessageModeSerializer(snippets, many=True)
        return Response(serializer.data)

    # Отправка сообщения - API
    def post(self, request, format=None):
        serializer = MessageModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

