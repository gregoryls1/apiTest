# Generated by Django 2.0.6 on 2018-06-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=12)),
                ('ano', models.CharField(max_length=4)),
                ('sinopse', models.CharField(max_length=300)),
            ],
        ),
    ]
