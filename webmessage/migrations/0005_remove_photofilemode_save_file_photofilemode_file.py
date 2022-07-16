# Generated by Django 4.0.6 on 2022-07-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmessage', '0004_photofilemode_remove_messagemode_file_this'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photofilemode',
            name='save_file',
        ),
        migrations.AddField(
            model_name='photofilemode',
            name='file',
            field=models.FileField(default=1, upload_to='media', verbose_name='Фото-файл'),
            preserve_default=False,
        ),
    ]
