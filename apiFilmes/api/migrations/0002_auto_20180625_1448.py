# Generated by Django 2.0.6 on 2018-06-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmes',
            name='genero',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='filmes',
            name='sinopse',
            field=models.CharField(max_length=600),
        ),
    ]
