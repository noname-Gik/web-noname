from django.db import models


# Название кнопки
class ButtonMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопка'

    name = models.CharField('Название', max_length=50, null=True, blank=True)
    link = models.CharField('Ссылка', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class PhotoFile(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Фото-файл'
        verbose_name_plural = 'Фото-файл'

    file = models.FileField('Фото-файл', upload_to="media")
