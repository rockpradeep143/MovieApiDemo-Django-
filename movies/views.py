from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
# Create your views here.
from .models import Moviesdata
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviesdata.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviesdata.objects.filter(typ='action')
    serializer_class = MovieSerializer
class SuspenseViewSet(viewsets.ModelViewSet):
    queryset = Moviesdata.objects.filter(typ='suspense')
    serializer_class = MovieSerializer