# Generated by Django 2.2 on 2021-08-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='dt_created',
            field=models.DateTimeField(verbose_name='Date Created'),
        ),
    ]