# Generated by Django 5.0.4 on 2024-05-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0023_mcsadpmodel_mcsadqmodel_mcscdmodel_mcselgmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IsobjModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isobj', models.TextField()),
            ],
        ),
    ]
