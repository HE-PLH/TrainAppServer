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


from .models import Train, Station, TrainClass
from .serializers import TrainSerializer, StationSerializer, TrainClassSerializer
from .decorators import validate_train_data, validate_station_data, validate_train_class_data


# Create your views here.




@method_decorator(csrf_exempt, name='dispatch')
class ListCreateTrainView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_train_data
    def post(self, request, *args, **kwargs):
        a_tag = Train.objects.create(
            name=request.data["name"],
            capacity=request.data["capacity"],
            images=request.data["images"],


        )
        return Response(
            data=TrainSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class TrainDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_train = self.queryset.get(pk=kwargs["pk"])
            return Response(TrainSerializer(a_train).data)
        except Train.DoesNotExist:
            return Response(
                data={
                    "message": "Train with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_train_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = TrainSerializer()
            updated_train = serializer.update(a_tag, request.data)
            return Response(TrainSerializer(updated_train).data)
        except Train.DoesNotExist:
            return Response(
                data={
                    "message": "Train with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_train = self.queryset.get(pk=kwargs["pk"])
            a_train.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Train.DoesNotExist:
            return Response(
                data={
                    "message": "Train with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    

@method_decorator(csrf_exempt, name='dispatch')
class ListCreateStationView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_station_data
    def post(self, request, *args, **kwargs):
        a_tag = Station.objects.create(
            name=request.data["name"],
            capacity=request.data["capacity"],
            images=request.data["images"],


        )
        return Response(
            data=StationSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class StationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_station = self.queryset.get(pk=kwargs["pk"])
            return Response(StationSerializer(a_station).data)
        except Station.DoesNotExist:
            return Response(
                data={
                    "message": "Station with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_station_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = StationSerializer()
            updated_station = serializer.update(a_tag, request.data)
            return Response(StationSerializer(updated_station).data)
        except Station.DoesNotExist:
            return Response(
                data={
                    "message": "Station with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_station = self.queryset.get(pk=kwargs["pk"])
            a_station.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Station.DoesNotExist:
            return Response(
                data={
                    "message": "Station with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    

@method_decorator(csrf_exempt, name='dispatch')
class ListCreateTrainClassView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = TrainClass.objects.all()
    serializer_class = TrainClassSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_train_class_data
    def post(self, request, *args, **kwargs):
        a_tag = TrainClass.objects.create(
            name=request.data["name"],
            capacity=request.data["capacity"],
            images=request.data["images"],


        )
        return Response(
            data=TrainClassSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class TrainClassDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = TrainClass.objects.all()
    serializer_class = TrainClassSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_train_class = self.queryset.get(pk=kwargs["pk"])
            return Response(TrainClassSerializer(a_train_class).data)
        except TrainClass.DoesNotExist:
            return Response(
                data={
                    "message": "TrainClass with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_train_class_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = TrainClassSerializer()
            updated_train_class = serializer.update(a_tag, request.data)
            return Response(TrainClassSerializer(updated_train_class).data)
        except TrainClass.DoesNotExist:
            return Response(
                data={
                    "message": "TrainClass with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_train_class = self.queryset.get(pk=kwargs["pk"])
            a_train_class.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TrainClass.DoesNotExist:
            return Response(
                data={
                    "message": "TrainClass with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    
