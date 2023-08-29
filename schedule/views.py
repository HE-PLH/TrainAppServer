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


from .models import Schedule
from .serializers import ScheduleSerializer
from .decorators import validate_schedule_data


# Create your views here.




@method_decorator(csrf_exempt, name='dispatch')
class ListCreateScheduleView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_schedule_data
    def post(self, request, *args, **kwargs):
        a_tag = Schedule.objects.create(
            start=request.data["start"],
            end=request.data["end"],
            from_station=request.data["from_station"],
            to_station=request.data["to_station"],
            train=request.data["train"],


        )
        return Response(
            data=ScheduleSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class ScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_schedule = self.queryset.get(pk=kwargs["pk"])
            return Response(ScheduleSerializer(a_schedule).data)
        except Schedule.DoesNotExist:
            return Response(
                data={
                    "message": "Schedule with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_schedule_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = ScheduleSerializer()
            updated_schedule = serializer.update(a_tag, request.data)
            return Response(ScheduleSerializer(updated_schedule).data)
        except Schedule.DoesNotExist:
            return Response(
                data={
                    "message": "Schedule with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_schedule = self.queryset.get(pk=kwargs["pk"])
            a_schedule.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Schedule.DoesNotExist:
            return Response(
                data={
                    "message": "Schedule with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    
