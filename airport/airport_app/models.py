from django.db import models

from django.utils import timezone
# Create your models here.


class Airline(models.Model):
    name = models.CharField(max_length=50)
    no_of_seats = models.PositiveIntegerField(default=0)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    cost_per_seat = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_no = models.CharField(max_length=6, primary_key=True)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

    STATUS_CHOICES = [
        ('Going To Take Off', 'Going To Take Off'),
        ('Took Off', 'Took Off'),
        ('Landed', 'Landed'),
        ('Delayed', 'Delayed'),
    ]

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Going To Take Off')

    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.flight_no)


class Passenger(models.Model):
    passport_no = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    GENDER = [
        ('M', 'Male'),
        (' F', 'Female'),
        ('O', 'others')
    ]

    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    nationality = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to="gallery")
    STATUS = [
        ('Yes', 'Checked-In'),
        ('No', 'Not Checked-In'),
    ]
    checked_in_status = models.CharField(
        max_length=3, choices=STATUS, default='No')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return self.passport_no


class CrewMember(models.Model):
    name = models.CharField(max_length=50)
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    TYPE_CHOICES = [
        ('Pilot', 'Pilot'),
        ('Flight Attendant', 'Flight Attendant')
    ]

    Type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default='Flight Attendant')

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    invoice_no = models.CharField(max_length=10, primary_key=True)
    invoice_datetime = models.DateTimeField(default=timezone.now)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.invoice_no)
