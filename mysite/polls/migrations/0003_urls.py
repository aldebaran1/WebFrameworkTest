# Generated by Django 2.0.6 on 2018-07-11 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180711_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.IntegerField(default=0)),
            ],
        ),
    ]
