from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework import status
from rest_framework.views import APIView

from webmessage.models import FileMessageMode
from rest_framework.response import Response

from webmessage.serializer import FileMessageModeSerializer, FileMessageModeSerializer


def handle_uploaded_file(f):
    with open('files/media/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class MessageList(APIView):
    def get(self, request, format=None):
        snippets = FileMessageMode.objects.all()
        serializer = FileMessageModeSerializer(snippets, many=True)
        return Response(serializer.data)

    # Отправка сообщения - API
    def post(self, request, format=None):
        serializer = FileMessageModeSerializer(data=request.data)
        if serializer.is_valid():
            # handle_uploaded_file(request.FILES['docfile'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

