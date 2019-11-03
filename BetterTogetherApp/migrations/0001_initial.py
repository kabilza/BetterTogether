# Generated by Django 2.2.5 on 2019-11-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('gender', models.CharField(max_length=1, verbose_name='Gender')),
                ('age', models.IntegerField(max_length=2, verbose_name='Age')),
            ],
        ),
        migrations.CreateModel(
            name='ShareRide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(verbose_name='Location')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_time', models.DateTimeField(verbose_name='Date and Time')),
                ('user', models.ManyToManyField(to='BetterTogetherApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='SharePromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(verbose_name='Location')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_time', models.DateTimeField(verbose_name='Date and Time')),
                ('user', models.ManyToManyField(to='BetterTogetherApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='ShareFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(verbose_name='Location')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_time', models.DateTimeField(verbose_name='Date and Time')),
                ('user', models.ManyToManyField(to='BetterTogetherApp.User')),
            ],
        ),
    ]
