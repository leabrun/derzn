# Generated by Django 3.2.4 on 2023-09-17 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drevo', '0072_merge_0071_alter_appeal_subject_0071_relation_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZnFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='files/%Y/%m/%d/', verbose_name='Файл')),
                ('znanie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='drevo.znanie')),
            ],
        ),
        migrations.CreateModel(
            name='AlgorithmData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_type', models.CharField(choices=[('active', 'Активный'), ('completed', 'Завершенный'), ('available', 'Доступный')], max_length=255, verbose_name='Тип элемента')),
                ('work_name', models.CharField(max_length=255, verbose_name='Работа')),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passed_algorithm', to='drevo.znanie', verbose_name='Алгоритм')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='algorithm_element', to='drevo.znanie', verbose_name='Элемент')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Данные алгоритма',
                'verbose_name_plural': 'Данные алгоритмов',
            },
        ),
    ]
