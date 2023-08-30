from django.urls import path
from .views import ListCreateTutorialView, TutorialDetailView

urlpatterns = [
    path('tutorial/', ListCreateTutorialView.as_view(), name="Tutorial-list-create"),
    path('tutorial/<int:pk>/', TutorialDetailView.as_view(), name="Tutorial-detail"),
    
]
