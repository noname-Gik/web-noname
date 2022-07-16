# Generated by Django 4.0.6 on 2022-07-16 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmessage', '0005_remove_photofilemode_save_file_photofilemode_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photofilemode',
            options={'ordering': ['id'], 'verbose_name': 'Загружаемый фото-файл', 'verbose_name_plural': 'Загружаемый фото-файл'},
        ),
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