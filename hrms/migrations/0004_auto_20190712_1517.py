# Generated by Django 2.2.2 on 2019-07-12 15:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0003_auto_20190712_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='first_in',
            field=models.TimeField(verbose_name=1562944628.7218237),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='last_out',
            field=models.TimeField(verbose_name=1562944628.7218492),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'), ('UNAVAILABLE', 'UNAVAILABLE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp803', max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=10),
        ),
        migrations.AlterField(
            model_name='employee',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 12, 15, 17, 8, 720922, tzinfo=utc)),
        ),
    ]