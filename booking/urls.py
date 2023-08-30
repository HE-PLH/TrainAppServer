from django.urls import path
from .views import ListCreateBookingView, BookingDetailView, ConfirmOrderView, getUserBookings

urlpatterns = [
    path('confirm-order/', ConfirmOrderView.as_view(), name="confirm-order-list-create"),
    path('get-user-bookings/', getUserBookings.as_view(), name="get-user-bookings-list-create"),

    path('booking/', ListCreateBookingView.as_view(), name="Booking-list-create"),
    path('booking/<int:pk>/', BookingDetailView.as_view(), name="Booking-detail"),
    
]
