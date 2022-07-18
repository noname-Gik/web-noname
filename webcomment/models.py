from django.db import models


# Комментарий - често хз почему возникает проблема с датой
class СommentMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'

    comment = models.CharField('Комментарий', max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.comment
