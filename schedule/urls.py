from django.urls import path
from .views import ListCreateScheduleView, ScheduleDetailView

urlpatterns = [
    path('schedule/', ListCreateScheduleView.as_view(), name="Schedule-list-create"),
    path('schedule/<int:pk>/', ScheduleDetailView.as_view(), name="Schedule-detail"),
    
]
