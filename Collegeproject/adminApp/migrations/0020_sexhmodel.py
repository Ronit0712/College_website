# Generated by Django 5.0.4 on 2024-05-02 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0019_eleobjmodel_elerolmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SexhModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexhdis', models.TextField()),
            ],
        ),
    ]
