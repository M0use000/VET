from django.urls import path
from . import views

urlpatterns = [
    path('', views.kazan_home),
    path('kazan', views.kazan_home),
    path('moscow', views.moscow_home),
    path('appointment', views.kazan_appointment),
    path('appointmentMOSCOW', views.appointmentMOSCOW),
    path("create1/", views.create1),
    path("rrr/", views.rrr),
    path("create3/", views.create3),
]
