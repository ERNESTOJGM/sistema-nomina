from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import RegistroForm

def home(request):
    return render(request, "home.html")

def registro(request):
    if request.user.is_authenticated:
        return redirect("users:dashboard")
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada. Inicia sesion.")
            return redirect("users:login")
    else:
        form = RegistroForm()
    return render(request, "users/register.html", {"form": form})

@login_required
def dashboard(request):
    user = request.user
    if user.is_superuser:
        rol = "Administrador"
    elif user.groups.filter(name="Gestor").exists():
        rol = "Gestor"
    elif user.groups.filter(name="Usuario").exists():
        rol = "Usuario"
    else:
        rol = "Sin rol"
    return render(request, "users/dashboard.html", {"rol": rol})