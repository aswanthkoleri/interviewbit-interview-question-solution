# Generated by Django 2.1.7 on 2019-09-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assigner', '0002_auto_20190927_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='dateTime',
            field=models.DateField(),
        ),
    ]
