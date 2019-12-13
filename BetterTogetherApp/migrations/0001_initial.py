<<<<<<< HEAD
# Generated by Django 2.2.5 on 2019-12-13 09:04

=======
>>>>>>> 0d26be3efffc984fdef6887e31f8bd3ed07f7510
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1, verbose_name='Gender (F or M)')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('brief_info', models.TextField(default='', verbose_name='Background Infomation')),
                ('phone_num', models.CharField(default=0, max_length=10, verbose_name='Phone Number')),
                ('twitter', models.TextField(blank=True, verbose_name='Twitter')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShareRide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.TextField(default='', verbose_name='Location Name')),
                ('location', models.TextField(default='', verbose_name='Location')),
                ('destination_name', models.TextField(default='', verbose_name='Destination Name')),
                ('destination', models.TextField(default='', verbose_name='Destination')),
                ('description', models.TextField(default='', max_length=80, verbose_name='Description')),
                ('date_time', models.DateTimeField(default='2019-12-13 16:04:38', verbose_name='Date and Time')),
                ('num_people', models.IntegerField(default=2, verbose_name='Number of people')),
                ('host', models.CharField(default='', max_length=30, verbose_name="Host's Name")),
                ('host_gender', models.CharField(max_length=1, verbose_name='Host Gender (F or M)')),
                ('full', models.BooleanField(default=False)),
                ('participants', models.ManyToManyField(to='BetterTogetherApp.Info')),
            ],
        ),
        migrations.CreateModel(
            name='SharePromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.TextField(default='', verbose_name='Location Name')),
                ('location', models.TextField(default='', verbose_name='Location')),
                ('brand', models.TextField(default='', verbose_name='Brand')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('date_time', models.DateTimeField(verbose_name='Date and Time')),
                ('num_people', models.IntegerField(default=2, verbose_name='Number of people')),
                ('host', models.CharField(default='', max_length=30, verbose_name="Host's Name")),
                ('host_gender', models.CharField(max_length=1, verbose_name='Host Gender (F or M)')),
                ('full', models.BooleanField(default=False)),
                ('participants', models.ManyToManyField(to='BetterTogetherApp.Info')),
            ],
        ),
        migrations.CreateModel(
            name='ShareFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.TextField(default='', verbose_name='Location Name')),
                ('location', models.TextField(default='', verbose_name='Location')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('date_time', models.DateTimeField(auto_now=True, verbose_name='Date and Time')),
                ('num_people', models.IntegerField(default=2, verbose_name='Number of people')),
                ('host', models.CharField(default='', max_length=30, verbose_name="Host's Name")),
                ('host_gender', models.CharField(max_length=1, verbose_name='Host Gender (F or M)')),
                ('full', models.BooleanField(default=False)),
                ('participants', models.ManyToManyField(to='BetterTogetherApp.Info')),
            ],
        ),
    ]
