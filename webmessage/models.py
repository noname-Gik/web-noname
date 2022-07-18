from django.db import models


# Сообщение-Файл - често хз почему возникает проблема с датой
class FileMessageMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Сообщения-файлы'
        verbose_name_plural = 'Сообщения-файлы'

    textsend = models.CharField('Содержание', max_length=25, null=True, blank=True)
    docfile = models.FileField('Фото-файл', upload_to="", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.textsend
