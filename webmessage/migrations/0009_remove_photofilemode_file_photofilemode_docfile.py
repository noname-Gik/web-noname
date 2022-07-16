# Generated by Django 4.0.6 on 2022-07-16 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmessage', '0008_photofilemode_alter_messagemode_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photofilemode',
            name='file',
        ),
        migrations.AddField(
            model_name='photofilemode',
            name='docfile',
            field=models.FileField(default=1, upload_to='', verbose_name='Фото-файл'),
            preserve_default=False,
        ),
    ]