# Generated by Django 2.0.6 on 2018-07-13 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_question_madid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
    ]
