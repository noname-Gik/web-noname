from django.db import models


# Сообщение-Файл
class FileMessageMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщение'

    textsend = models.CharField('Содержание', max_length=100, null=True, blank=True)
    docfile = models.FileField('Фото-файл', upload_to="", null=True, blank=True)
