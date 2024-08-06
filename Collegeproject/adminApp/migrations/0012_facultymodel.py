# Generated by Django 5.0.4 on 2024-05-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0011_adminimodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('fspeci', models.CharField(max_length=100)),
                ('fdepart', models.CharField(max_length=100)),
                ('fimg', models.FileField(upload_to='static/uploads/')),
            ],
        ),
    ]
