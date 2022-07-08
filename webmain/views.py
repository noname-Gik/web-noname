from django.shortcuts import render

from webmain.models import ButtonMode, PhotoFile


def home(request):
    photofilesmain = PhotoFile.objects.filter(id=1)
    buttonlist = ButtonMode.objects.all()
    return render(request, 'home.html', {'photofilesmain': photofilesmain, 'buttonlist': buttonlist})
