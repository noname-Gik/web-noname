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


# Название совета
class AdviceMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Совет'
        verbose_name_plural = 'Совет'

    name = models.CharField('Название', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# Название совета
class TicketMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Подсказка'
        verbose_name_plural = 'Подсказка'

    name = models.CharField('Название', max_length=100, null=True, blank=True)
    navzone = models.CharField('Содержание', max_length=10, null=True, blank=True)

    def __str__(self):
        return self.navzone


class PhotoFile(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Фото-файл'
        verbose_name_plural = 'Фото-файл'

    file = models.FileField('Фото-файл', upload_to="media")
