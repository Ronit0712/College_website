# Generated by Django 5.0.4 on 2024-04-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hvideo', models.FileField(upload_to='')),
            ],
        ),
    ]
