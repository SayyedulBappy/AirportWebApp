from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_flights', views.view_flights, name='view_flights'),
    path('search_by_source', views.search_by_source, name='search_by_source'),
    path('search_by_destination', views.search_by_destination,
         name='search_by_destination'),
    path('view_available_flights/', views.view_available_flights,
         name='view_available_flights'),
    path('book_flight/<str:pk>', views.book_flight, name='book_flight'),
    path('passenger_home/<invoice_no>',
         views.passenger_home, name='passenger_home'),
    path('view_booking', views.view_booking, name='view_booking'),
]
