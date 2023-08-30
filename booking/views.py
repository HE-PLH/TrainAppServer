from django.contrib.auth.models import User
from django.db.models import Prefetch, Subquery, OuterRef
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from schedule.models import Schedule
from .models import Booking, BookingItem
from .serializers import BookingSerializer, BookingItemSerializer
from .decorators import validate_booking_data


# Create your views here.




@method_decorator(csrf_exempt, name='dispatch')
class ListCreateBookingView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_booking_data
    def post(self, request, *args, **kwargs):
        a_tag = Booking.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            images=request.data["images"],


        )
        return Response(
            data=BookingSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_booking = self.queryset.get(pk=kwargs["pk"])
            return Response(BookingSerializer(a_booking).data)
        except Booking.DoesNotExist:
            return Response(
                data={
                    "message": "Booking with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_booking_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = BookingSerializer()
            updated_booking = serializer.update(a_tag, request.data)
            return Response(BookingSerializer(updated_booking).data)
        except Booking.DoesNotExist:
            return Response(
                data={
                    "message": "Booking with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_booking = self.queryset.get(pk=kwargs["pk"])
            a_booking.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Booking.DoesNotExist:
            return Response(
                data={
                    "message": "Booking with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
class ConfirmOrderView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_booking_data
    def post(self, request, *args, **kwargs):
        bookings = request.data["bookings"]
        user = User.objects.get(id=request.data["user"])


        ticket_owner_details = request.data["ticket_owner_details"]
        if len(bookings):
            my_booking = Booking.objects.create(
                user=user,
                # order_date=request.data["order_date"],
                paid='Not Paid',
                name=ticket_owner_details["name"],
                county=ticket_owner_details["county"],
                city=ticket_owner_details["city"],
                phone=ticket_owner_details["phone"]
            )

            booking_items = [BookingItem.objects.create(
                schedule=Schedule.objects.get(id=bk['id']),
                booking=my_booking,
                seats=bk["qty"],
                price=bk["price"]
            ) for bk in bookings]


            return Response(
                data={'booking': BookingSerializer(my_booking).data,
                      'booking_items':
                          BookingItemSerializer(booking_items, many=True).data,
                      },
                    status=status.HTTP_201_CREATED
                )

        else:
            return Response(
                data={},
                status=status.HTTP_204_NO_CONTENT
            )
        
        
    
