# Generated by Django 3.2.4 on 2024-02-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0117_auto_20240201_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='var',
            name='structure',
            field=models.IntegerField(choices=[(0, 'Переменная'), (1, 'Массив'), (2, 'Итератор'), (3, 'Условие')], default=0, verbose_name='Тип объекта'),
        ),
    ]