from django.shortcuts import render
from rest_framework import viewsets
from .models import Port
from .serializers import PortSerializer


# Create your views here.

# ViewSets define the view behavior.
class PortViewSet(viewsets.ModelViewSet):
    # queryset = Port.objects.all().order_by('-time')
    queryset = Port.objects.all()
    serializer_class = PortSerializer
    # permission_classes = (AllowAny,)
