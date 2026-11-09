from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import EmpleadoForm
from .models import Empleado

def _puede_gestionar(user):
    return user.is_superuser or user.groups.filter(name="Gestor").exists()

@login_required
def lista_empleados(request):
    q = request.GET.get("q", "").strip()
    empleados = Empleado.objects.all()
    if q:
        empleados = empleados.filter(nombre__icontains=q) | empleados.filter(cedula__icontains=q)
    return render(request, "core/lista_empleados.html", {
        "empleados": empleados,
        "busqueda": q,
        "puede_gestionar": _puede_gestionar(request.user),
    })

@login_required
def detalle_empleado(request, cedula):
    emp = get_object_or_404(Empleado, cedula=cedula)
    return render(request, "core/detalle_empleado.html", {"emp": emp})

@login_required
def nuevo_empleado(request):
    if not _puede_gestionar(request.user):
        messages.error(request, "Sin permiso.")
        return redirect("core:lista")
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            emp = form.save(commit=False)
            emp.usuario = request.user
            emp.save()
            messages.success(request, "Empleado registrado.")
            return redirect("core:lista")
    else:
        form = EmpleadoForm()
    return render(request, "core/nuevo_empleado.html", {"form": form})

@login_required
def editar_empleado(request, cedula):
    if not _puede_gestionar(request.user):
        messages.error(request, "Sin permiso.")
        return redirect("core:lista")
    emp = get_object_or_404(Empleado, cedula=cedula)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            messages.success(request, "Empleado actualizado.")
            return redirect("core:lista")
    else:
        form = EmpleadoForm(instance=emp)
    return render(request, "core/editar_empleado.html", {"form": form, "emp": emp})

@login_required
def eliminar_empleado(request, cedula):
    if not _puede_gestionar(request.user):
        messages.error(request, "Sin permiso.")
        return redirect("core:lista")
    emp = get_object_or_404(Empleado, cedula=cedula)
    if request.method == "POST":
        emp.delete()
        messages.success(request, "Empleado eliminado.")
    return redirect("core:lista")