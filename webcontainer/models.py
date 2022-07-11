from django.db import models


# Организация
class OrganizationTableMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Организация'
        verbose_name_plural = 'Организация'

    name = models.CharField('Название организации', max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


# Роль
class RoleTableMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Роль'
        verbose_name_plural = 'Роль'

    name = models.CharField('Название роли', max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


# Пользователь
class UserTableMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'

    firstname = models.CharField('Фамилия', max_length=25, null=False, blank=False)
    mainname = models.CharField('Имя', max_length=20, null=False, blank=False)
    lastname = models.CharField('Отчество', max_length=25, null=True, blank=True)

    def __str__(self):
        return self.firstname + ' ' + self.mainname + ' ' + self.lastname


# Организация-Роль-Пользователь
class ConnectionTableMode(models.Model):
    class Meta:
        ordering = ['id', ]
        verbose_name = 'Организация-Роль-Пользователь'
        verbose_name_plural = 'Организация-Роль-Пользователь'

    organizations = models.ForeignKey(OrganizationTableMode, verbose_name='Организация', on_delete=models.CASCADE,
                                      null=True, blank=True)
    roles = models.ForeignKey(RoleTableMode, verbose_name='Роль', on_delete=models.CASCADE, null=True, blank=True)
    users = models.ForeignKey(UserTableMode, verbose_name='Пользователь', on_delete=models.CASCADE, null=True,
                              blank=True)

    def __str__(self):
        return f"{self.users.firstname} {self.users.mainname} {self.users.lastname}"


