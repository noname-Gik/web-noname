from django.db import models


# Сообщение
class MessageMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщение'

    textsend = models.CharField('Содержание', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.textsend


# Файл
class PhotoFileMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Фото-файл'
        verbose_name_plural = 'Фото-файл'

    file = models.FileField('Фото-файл', upload_to="media")
