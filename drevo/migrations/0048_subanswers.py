# Generated by Django 4.1.1 on 2023-02-07 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drevo', '0047_alter_knowledgestatuses_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_answer', models.TextField(verbose_name='Подответ')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answ_sub_answers', to='drevo.znanie', verbose_name='Ответ')),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_answers', to=settings.AUTH_USER_MODEL, verbose_name='Эксперт')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_sub_answers', to='drevo.znanie', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Подответ',
                'verbose_name_plural': 'Подответы',
            },
        ),
    ]