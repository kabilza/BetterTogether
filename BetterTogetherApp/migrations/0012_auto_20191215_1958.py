# Generated by Django 2.2.5 on 2019-12-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BetterTogetherApp', '0011_auto_20191215_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharefood',
            name='date_time',
            field=models.TextField(default='2019-12-15 19:58:59', verbose_name='Date and Time'),
        ),
        migrations.AlterField(
            model_name='sharepromotion',
            name='date_time',
            field=models.TextField(default='2019-12-15 19:58:59', verbose_name='Date and Time'),
        ),
        migrations.AlterField(
            model_name='shareride',
            name='date_time',
            field=models.TextField(default='2019-12-15 19:58:59', verbose_name='Date and Time'),
        ),
    ]
