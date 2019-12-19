from django.shortcuts import render, redirect, get_object_or_404

from .models import *


from random import randint
# Create your views here.


def home(request):
    return render(request, 'airport_app/home.html')


def view_flights(request):
    data = Flight.objects.order_by('flight_no')
    return render(request, 'airport_app/view_flights.html', {'flights': data})


def search_by_source(request):
    if request.method == "POST":
        source = request.POST['source']
        if source:
            data = Flight.objects.filter(airline__source=source)
            return render(request, 'airport_app/view_flights.html', {'flights': data})
        else:
            return redirect('view_flights')
    else:
        return redirect('view_flights')


def search_by_destination(request):
    if request.method == "POST":
        destination = request.POST['destination']
        if destination:
            data = Flight.objects.filter(airline__destination=destination)
            return render(request, 'airport_app/view_flights.html', {'flights': data})
        else:
            return redirect('view_flights')
    else:
        return redirect('view_flights')


def view_available_flights(request):
    if request.method == "POST":
        source = request.POST['source']
        destination = request.POST['destination']
        if source and destination:
            flights = Flight.objects.filter(
                airline__source=source, airline__destination=destination)
            if flights:
                return render(request, 'airport_app/home.html', {'flights': flights})
            else:
                return render(request, 'airport_app/home.html', {'error_message_flight': "No flights found"})
        else:
            return redirect('home')
    else:
        return redirect('home')


def book_flight(request, pk):
    if request.method == "POST":
        flight = Flight.objects.get(flight_no=pk)

        passport_no = request.POST['passport_no']
        name = request.POST['name']
        nationality = request.POST['nationality']
        gender = request.POST['gender']
        contact_no = request.POST['contact_no']
        email = request.POST['email']
        image = request.FILES['image']

        passenger = Passenger(passport_no=passport_no, name=name, nationality=nationality,
                              gender=gender, contact_no=contact_no, email=email, image=image, flight=flight)
        invoice = Invoice(invoice_no=randint(
            1000000000, 9999999999), passenger=passenger)
        passenger.save()
        invoice.save()
        flight.airline.no_of_seats -= 1
        flight.save()
        return redirect('passenger_home', invoice_no=invoice.pk)
    else:
        return render(request, 'airport_app/book_flight.html', {'flight_no': pk})


def passenger_home(request, invoice_no):
    invoice = Invoice.objects.get(invoice_no=invoice_no)
    return render(request, 'airport_app/passenger_home.html', {'invoice': invoice})


def view_booking(request):
    if request.method == "POST":  # view existing booking
        passport_no = request.POST['passport_no']
        try:
            passenger = Passenger.objects.get(passport_no=passport_no)
        except Passenger.DoesNotExist:
            passenger = None
        if passenger:
            invoice = get_object_or_404(Invoice, passenger=passport_no)
            return render(request, 'airport_app/passenger_home.html', {'invoice': invoice})
        else:
            return render(request, 'airport_app/home.html', {'error_message_booking': 'No booking found'})
