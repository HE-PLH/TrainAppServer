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


from .models import Tutorial
from .serializers import TutorialSerializer
from .decorators import validate_tutorial_data


# Create your views here.




@method_decorator(csrf_exempt, name='dispatch')
class ListCreateTutorialView(generics.ListCreateAPIView):
    """
    GET Chats/
    POST Chats/
    """
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_tutorial_data
    def post(self, request, *args, **kwargs):
        a_tag = Tutorial.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            images=request.data["images"],


        )
        return Response(
            data=TutorialSerializer(a_tag).data,
            status=status.HTTP_201_CREATED
        )



class TutorialDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Chats/:id/
    PUT Chats/:id/
    DELETE Chats/:id/
    """
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            a_tutorial = self.queryset.get(pk=kwargs["pk"])
            return Response(TutorialSerializer(a_tutorial).data)
        except Tutorial.DoesNotExist:
            return Response(
                data={
                    "message": "Tutorial with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_tutorial_data
    def put(self, request, *args, **kwargs):
        try:
            a_tag = self.queryset.get(pk=kwargs["pk"])
            serializer = TutorialSerializer()
            updated_tutorial = serializer.update(a_tag, request.data)
            return Response(TutorialSerializer(updated_tutorial).data)
        except Tutorial.DoesNotExist:
            return Response(
                data={
                    "message": "Tutorial with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_tutorial = self.queryset.get(pk=kwargs["pk"])
            a_tutorial.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Tutorial.DoesNotExist:
            return Response(
                data={
                    "message": "Tutorial with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        
    
