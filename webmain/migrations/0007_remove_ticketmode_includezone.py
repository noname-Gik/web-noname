# Generated by Django 4.0.6 on 2022-07-09 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webmain', '0006_ticketmode_includezone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketmode',
            name='includezone',
        ),
    ]