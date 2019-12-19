# Generated by Django 2.2.6 on 2019-11-02 10:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('no_of_seats', models.PositiveIntegerField(default=0)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('Class', models.CharField(choices=[('Economy', 'Economy'), ('Business', 'Business')], default='Economy', max_length=8)),
                ('cost_per_seat', models.DecimalField(decimal_places=2, default=500.0, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_no', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('arrival_time', models.DateTimeField()),
                ('departure_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Going To Take Off', 'Going To Take Off'), ('Took Off', 'Took Off'), ('Landed', 'Landed'), ('Delayed', 'Delayed')], default='Going To Take Off', max_length=20)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport_app.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('passport_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('nationality', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport_app.Flight')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('invoice_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('passport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport_app.Passenger')),
            ],
        ),
        migrations.CreateModel(
            name='CrewMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('Type', models.CharField(choices=[('Pilot', 'Pilot'), ('Flight Attendant', 'Flight Attendant')], default='Flight Attendant', max_length=10)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airport_app.Flight')),
            ],
        ),
    ]