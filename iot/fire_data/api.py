from rest_framework import viewsets
from .models import Data
from .serielizers import DataSerializer 

class DataViewSet(viewsets.ModelViewSet):

    queryset = Data.objects.all()
    serializer_class = DataSerializer
    