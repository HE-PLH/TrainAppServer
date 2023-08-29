from django.urls import path
from mpesa import views
from mpesa.views import ListCreateMpesaView

urlpatterns = [
    path('mpesa/', ListCreateMpesaView.as_view(), name="Mpesa-list-create"),
    # path('mpesa/', views.mpesa_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
]