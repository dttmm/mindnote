# Generated by Django 2.2 on 2021-08-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20210804_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='dt_created',
            field=models.DateTimeField(verbose_name='Date Created'),
        ),
    ]
