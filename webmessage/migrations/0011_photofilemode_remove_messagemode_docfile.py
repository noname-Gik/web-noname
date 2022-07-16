# Generated by Django 4.0.6 on 2022-07-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmessage', '0010_delete_photofilemode_messagemode_docfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoFileMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='media', verbose_name='Фото-файл')),
            ],
            options={
                'verbose_name': 'Фото-файл',
                'verbose_name_plural': 'Фото-файл',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='messagemode',
            name='docfile',
        ),
    ]
