# Generated by Django 4.0.6 on 2022-07-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmessage', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhotoFileMode',
        ),
        migrations.AddField(
            model_name='messagemode',
            name='file',
            field=models.FileField(default=1, upload_to='media', verbose_name='Фото-файл'),
            preserve_default=False,
        ),
    ]