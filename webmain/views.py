from django.shortcuts import render
from django.db.models import Q
from webmain.models import ButtonMode, PhotoFile, AdviceMode, TicketMode

advicelist = AdviceMode.objects.filter()


def home(request):
    photofilesmain = PhotoFile.objects.filter(id=1)
    buttonlist = ButtonMode.objects.filter()
    return render(request, 'webmain/securitycontainPR/htmlcard.html',
                  {'photofilesmain': photofilesmain, 'advicelist': advicelist, 'buttonlist': buttonlist})


def advice_home(request):
    mainticket = TicketMode.objects.filter(id=1)
    secondaryticket = TicketMode.objects.filter(~Q(id=1))
    return render(request, 'webmain/securitycontainPR/htmladvice.html',
                  {'mainticket': mainticket, 'secondaryticket': secondaryticket, 'advicelist': advicelist})
