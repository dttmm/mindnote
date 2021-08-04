# Generated by Django 2.2 on 2021-08-04 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('feelings', models.CharField(max_length=80)),
                ('score', models.IntegerField()),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
            ],
        ),
    ]