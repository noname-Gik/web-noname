# Generated by Django 4.0.6 on 2022-07-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webmessage', '0007_delete_photofilemode_alter_messagemode_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoFileMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media', verbose_name='Фото-файл')),
            ],
            options={
                'verbose_name': 'Фото-файл',
                'verbose_name_plural': 'Фото-файл',
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='messagemode',
            options={'ordering': ['id'], 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщение'},
        ),
        migrations.RemoveField(
            model_name='messagemode',
            name='docfile',
        ),
    ]