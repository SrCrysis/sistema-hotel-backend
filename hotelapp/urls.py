from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'huespedes', views.HuespedViewSet)
router.register(r'habitaciones', views.HabitacionViewSet)
router.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('api/', include(router.urls)),
]