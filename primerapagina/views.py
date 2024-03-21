from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import OrdenForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def holamundo(request):
    return HttpResponse("Hola Mundo")

def home(request):
    return render(request,"home.html")
def registro(request):
    if request.method =='GET' :
        return render(request,"registro.html", {
            "form":UserCreationForm
        })
    else:
        req=request.POST
        if req['password1'] ==req['password2']:
            try:
                user= User.objects.create_user(
                    username=req['username'],
                    password=req['password1']
                )
                user.save()
                login(request,user)
                return redirect('/')
            except IntegrityError as ie:
                return render(request,"registro.html", {
                "form":UserCreationForm,
                "msg":"Ese usuario ya existe, favor de elegir otro nombre de usuario"
            })
            except Exception as e:
                return render(request,"registro.html", {
                "form":UserCreationForm,
                "msg":f"Se ha presentado el siguiente error {e}"
            })
        else:
            return render(request,"registro.html", {
            "form":UserCreationForm,
            "msg":"Favor de verificar que las contraseñas coicidan"
        })

def iniciarsesion(request):
    if request.method=="GET":
        return render(request, "login.html",{
            "form": AuthenticationForm,
        })
    else:
        try:
            user=authenticate(request,
                            username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                return render(request, "login.html",{
                "form": AuthenticationForm,
                "msg": "El usuario o la contraseña son incorrectas"
            })
        except Exception as e:
            return render(request, "login.html",{
                "form": AuthenticationForm,
                "msg": f"Hubo un error{e}"
            })
def cerrarsesion(request):
    logout(request)
    return redirect("/")
@login_required
def nuevaOrden(request):
    if request.method=="GET":
        return render(request, "nuevaorden.html",{
                    "form": OrdenForm
                })
    else:
        try:
            form=OrdenForm(request.POST)
            if form.is_valid():
                nuevo=form.save(commit=False)
                if request.user.is_authenticated:
                    nuevo.usuario=request.user
                    nuevo.save()
                    return redirect("/")
                else:
                    return render(request, "nuevaorden.html",{
                        "form": OrdenForm,
                        "msg":"Usted debe autenticarse"
                    })

            else:
                return render(request, "nuevaorden.html",{
                        "form": OrdenForm,
                        "msg":"Este formulario no es valido"
                    })
        except Exception as e:
            return render(request, "nuevaorden.html",{
                        "form": OrdenForm,
                        "msg":f"Hubo un error {e}"
                    })