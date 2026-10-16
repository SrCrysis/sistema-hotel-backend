from django.shortcuts import render
from rest_framework import viewsets

from .models import Huesped, Habitacion, Reserva
from .serializers import (
    HuespedSerializer,
    HabitacionSerializer,
    ReservaSerializer,
)


def bienvenida(request):
    return render(request, 'hotelapp/bienvenida.html')


class HuespedViewSet(viewsets.ModelViewSet):
    queryset = Huesped.objects.all()
    serializer_class = HuespedSerializer


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer