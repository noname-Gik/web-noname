from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from webcontainer.models import ConnectionTableMode
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
    # поиск по слову в таблице
    sett_search = {}
    datalist = ConnectionTableMode.objects.filter()
    if request.GET.get('search_name'):
        sett_search['search_name'] = request.GET.get('search_name')
        datalist = datalist.filter(Q(organizations__name__icontains=request.GET.get('search_name')) |
                                   Q(roles__name__icontains=request.GET.get('search_name')) |
                                   Q(users__firstname__icontains=request.GET.get('search_name')))
    else:
        # Используется ограничение вывода из database
        datalist = datalist[0:50]
    # пагинация для таблицы
    page = request.GET.get('page', 1)
    paginator = Paginator(datalist, 5)
    try:
        datausers = paginator.page(page)
    except PageNotAnInteger:
        datausers = paginator.page(1)
    except EmptyPage:
        datausers = paginator.page(paginator.num_pages)
    return render(request, 'webmain/securitycontainPR/htmladvice.html',
                  {'mainticket': mainticket, 'secondaryticket': secondaryticket, 'advicelist': advicelist,
                   'datausers': datausers, 'sett_search': sett_search, })

