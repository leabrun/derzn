# Generated by Django 3.2.4 on 2022-10-04 07:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import drevo.models.interview_answer_expert_proposal


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("drevo", "0022_tz_is_send"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="interviewanswerexpertproposal",
            name="is_yesno_answer_argument",
        ),
        migrations.RemoveField(
            model_name="interviewanswerexpertproposal",
            name="согласен",
        ),
        migrations.AddField(
            model_name="interviewanswerexpertproposal",
            name="interview",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="interview_proposals",
                to="drevo.znanie",
                verbose_name="Интервью",
            ),
        ),
        migrations.AddField(
            model_name="interviewanswerexpertproposal",
            name="is_agreed",
            field=models.BooleanField(
                default=True, verbose_name="Эксперт согласен с ответом?"
            ),
        ),
        migrations.AddField(
            model_name="interviewanswerexpertproposal",
            name="question",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="question_proposals",
                to="drevo.znanie",
            ),
        ),
        migrations.AlterField(
            model_name="interviewanswerexpertproposal",
            name="admin_comment",
            field=models.TextField(
                blank=True, default="", verbose_name="Комментарий администратора"
            ),
        ),
        migrations.AlterField(
            model_name="interviewanswerexpertproposal",
            name="admin_reviewer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Администратор",
            ),
        ),
        migrations.AlterField(
            model_name="interviewanswerexpertproposal",
            name="answer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="answer_proposals",
                to="drevo.znanie",
                verbose_name="Ответ",
            ),
        ),
        migrations.AlterField(
            model_name="interviewanswerexpertproposal",
            name="comment",
            field=models.JSONField(
                blank=True,
                default=drevo.models.interview_answer_expert_proposal.comment_default_factory,
                null=True,
                verbose_name="Аргументы и контраргументы (JSON)",
            ),
        ),
        migrations.AlterField(
            model_name="interviewanswerexpertproposal",
            name="is_incorrect_answer",
            field=models.BooleanField(default=False, verbose_name="некорректный ответ"),
        ),
        migrations.AlterField(
            model_name="interviewanswerexpertproposal",
            name="new_answer",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="made_in_interview",
                to="drevo.znanie",
                verbose_name="Новый ответ",
            ),
        ),
        migrations.AlterField(
            model_name="interviewanswerexpertproposal",
            name="new_answer_text",
            field=models.TextField(
                blank=True, null=True, verbose_name="новый ответ от эксперта"
            ),
        ),
        migrations.AlterField(
            model_name="interviewanswerexpertproposal",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("APPRVE", "Принят"),
                    ("REJECT", "Не принят"),
                    ("ANSDPL", "Дублирует ответ"),
                    ("RESDPL", "Дублирует предложение"),
                ],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="interviewanswerexpertproposal",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddConstraint(
            model_name="interviewanswerexpertproposal",
            constraint=models.UniqueConstraint(
                fields=("answer", "expert", "interview", "question"),
                name="single_proposal_from_expert_on_answer",
            ),
        ),
    ]