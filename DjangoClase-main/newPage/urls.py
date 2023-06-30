from django.urls import path
from . import views

urlpatterns = [
    path("re4",views.bici1,name="bici1"),
    path("home",views.home,name="home"),
    path("contacto",views.contacto,name="contacto"),
    path("Bici4",views.bici4,name="Bici4"),
    path("Bici3",views.bici3,name="Bici3"),
    path("Bici2",views.bici2,name="Bici2"),
    path("Bici5",views.bici5,name="bici5"),
    path("seguridad",views.seguridad,name="seguridad"),
    path("catalogo",views.catalogo,name="catalogo"),
    path("navbar",views.nav,name="navbar"),
    path("Arreglo",views.arreglo,name="Arreglo"),
    path("inicio_sesion",views.inicio_sesion,name="inicio_sesion"),
    path("creacion_user",views.userAdd,name="creacion_user"),
]
