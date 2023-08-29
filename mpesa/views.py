from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from mpesa.models import Mpesa
from mpesa.serializers import MpesaSerializer
from  mpesa.lipanampesa import lipa_na_mpesa

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ListCreateMpesaView(generics.ListCreateAPIView):
    """
        GET Chats/
        POST Chats/
        """
    queryset = Mpesa.objects.all()
    serializer_class = MpesaSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        # tag_instance = Chats.objects.get()
        # a_pattern = ChatsSerializer.objects.create(
        #     name=request.data["name"]
        # )
        # Test the chatbot
        phone = request.data['phone_number']
        amount = request.data['amount']
        payBill = request.data['payBill']
        # here we run the function
        lipa_na_mpesa(phone, amount, payBill)
        # end of function
        # s= MpesaSerializer()

        # return JsonResponse(serializer.data, status=201)
        return Response(
            data='s.data',
            status=status.HTTP_201_CREATED
        )
# Create your views here.
# @csrf_exempt
# def mpesa_list(request):
#     """"
#     List  all mpesa calls
#     """
#     if request.method =="GET":
#         mpesas=Mpesa.objects.all()
#         serializer=MpesaSerializer(mpesas,many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method =="POST":
#         data = JSONParser().parse(request)
#         serializer=MpesaSerializer(data=data)
#         if serializer.is_valid():
#             phone=data['phone_number']
#             amount=data['amount']
#             payBill=data['payBill']
#             # here we run the function
#             lipa_na_mpesa(phone,amount,payBill)
#             # end of function
#             serializer.save()
#             print("The data is :",data)
#             print(request)
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse (serializer.errors, status=400)

