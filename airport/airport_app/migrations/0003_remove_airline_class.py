# Generated by Django 2.2.6 on 2019-11-02 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airport_app', '0002_auto_20191102_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airline',
            name='Class',
        ),
    ]
