from rest_framework import serializers, viewsets
from ..models import Digit
from .serializer import DigitSerializer

class DigitViewSet(viewsets.ModelViewSet):
  serializer_class = DigitSerializer
  queryset = Digit.objects.all()
  
  