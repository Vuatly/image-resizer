# Generated by Django 3.1 on 2020-08-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Название файла')),
                ('file', models.ImageField(blank=True, upload_to='', verbose_name='Файл с изображением')),
                ('resized', models.ImageField(blank=True, upload_to='', verbose_name='Изображение с измененным размером')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
