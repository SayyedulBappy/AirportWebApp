from django.contrib import admin

from .models import Airline, Flight, Passenger, CrewMember, Invoice
# Register your models here.

#  # a list of displayed columns name.
#     list_display = []

#     # define search columns list, then a search box will be added at the top of Department list page.
#     search_fields = []

#     # define filter columns list, then a filter widget will be shown at right side of Department list page.
#     list_filter = []
#     # define which field will be pre populated.
#     prepopulated_fields = {}
#     # define model data list ordering.
#     ordering = ()


class AirlineAdmin(admin.ModelAdmin):

    list_display = ['name', 'source', 'destination']
    search_fields = ['name', 'source', 'destination']
    list_filter = ['name', 'source', 'destination']


class FlightAdmin(admin.ModelAdmin):

    list_display = ['flight_no', 'departure_time', 'arrival_time',
                    'airline']
    search_fields = ['flight_no', 'departure_time', 'arrival_time', 'airline']
    list_filter = ['flight_no', 'departure_time', 'arrival_time', 'airline']


class PassengerAdmin(admin.ModelAdmin):

    list_display = ['passport_no', 'name', 'gender',
                    'nationality', 'contact_no', 'email', 'flight', 'checked_in_status']
    search_fields = ['passport_no', 'name', 'gender',
                     'nationality', 'contact_no', 'email', 'flight', 'checked_in_status']
    list_filter = ['passport_no', 'name', 'gender',
                   'nationality', 'contact_no', 'email', 'flight', 'checked_in_status']


class CrewMemberAdmin(admin.ModelAdmin):

    list_display = ['name', 'gender', 'Type', 'flight']
    search_fields = ['name', 'gender', 'Type', 'flight']
    list_filter = ['name', 'gender', 'Type', 'flight']


class InvoiceAdmin(admin.ModelAdmin):

    list_display = ['invoice_no', 'invoice_datetime', 'passenger']
    search_fields = ['invoice_no', 'invoice_datetime', 'passenger']
    list_filter = ['invoice_no', 'invoice_datetime', 'passenger']


admin.site.register(Airline, AirlineAdmin)

admin.site.register(Flight, FlightAdmin)

admin.site.register(Passenger, PassengerAdmin)

admin.site.register(CrewMember, CrewMemberAdmin)

admin.site.register(Invoice, InvoiceAdmin)
