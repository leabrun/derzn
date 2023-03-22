# Generated by Django 3.2.4 on 2023-03-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drevo', '0056_auto_20230311_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='knowledgegradescale',
            options={'ordering': ('order',), 'verbose_name': 'Градация', 'verbose_name_plural': 'Шкала оценок знаний'},
        ),
        migrations.AlterModelOptions(
            name='relationgradescale',
            options={'ordering': ('order',), 'verbose_name': 'Градация', 'verbose_name_plural': 'Шкала оценок связей'},
        ),
        migrations.AddField(
            model_name='relationgradescale',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Порядок'),
        ),
        migrations.AlterField(
            model_name='knowledgegradescale',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Порядок'),
        ),
    ]