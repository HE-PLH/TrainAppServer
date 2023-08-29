from django.urls import path
from .views import ListCreateTrainView, TrainDetailView, ListCreateStationView, StationDetailView

urlpatterns = [
    path('train/', ListCreateTrainView.as_view(), name="Train-list-create"),
    path('train/<int:pk>/', TrainDetailView.as_view(), name="Train-detail"),
    
    path('station/', ListCreateStationView.as_view(), name="Station-list-create"),
    path('station/<int:pk>/', StationDetailView.as_view(), name="Station-detail"),
    
]
