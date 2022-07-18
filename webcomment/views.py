from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from webcomment.models import СommentMode
from webcomment.serializer import СommentModeSerializer


# Работа с api
class CommentsList(APIView):
    def get(self, request, format=None):
        snippets = СommentMode.objects.all()
        serializer = СommentModeSerializer(snippets, many=True)
        return Response(serializer.data)

    # Отправка комментариев - API
    def post(self, request, format=None):
        serializer = СommentModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
