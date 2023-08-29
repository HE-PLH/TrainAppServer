from django.urls import path
from .views import ListCreateBookingView, BookingDetailView

urlpatterns = [
    path('booking/', ListCreateBookingView.as_view(), name="Booking-list-create"),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name="Booking-detail"),
    
]
