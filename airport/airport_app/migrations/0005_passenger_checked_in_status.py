# Generated by Django 2.2.6 on 2019-11-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport_app', '0004_auto_20191102_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='checked_in_status',
            field=models.CharField(choices=[('Yes', 'Checked-In'), ('No', 'Not Checked-In')], default='No', max_length=3),
        ),
    ]
