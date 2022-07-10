from django.urls import path, include

from . import views

from .views import advice_home

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.PhotoFile, name="PhotoFile"),
    # соединение с стр. advice_zone
    path('advice_zone/', advice_home, name='advice_home'),
]
