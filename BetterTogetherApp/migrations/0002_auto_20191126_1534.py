# Generated by Django 2.2.5 on 2019-11-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetterTogetherApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareride',
            name='date_time',
            field=models.DateTimeField(default='2019-11-26 15:34:52', verbose_name='Date and Time'),
        ),
    ]
