from django.urls import path
from .views import EventAPIView

urlpatterns = [
    path('events/', EventAPIView.as_view()),           # GET all, POST
    path('events/<int:pk>/', EventAPIView.as_view()),  # GET one, PUT, DELETE
]
