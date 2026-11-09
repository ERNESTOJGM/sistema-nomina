from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.lista_empleados, name="lista"),
    path("empleado/<str:cedula>/", views.detalle_empleado, name="detalle"),
    path("nuevo/", views.nuevo_empleado, name="nuevo"),
    path("editar/<str:cedula>/", views.editar_empleado, name="editar"),
    path("eliminar/<str:cedula>/", views.eliminar_empleado, name="eliminar"),
]