
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import mail, serializers

from .models import (Localidad, Spots, Decks,Wheels, Trucks, Order, Cart, ShippingAddress, Bearings, Hardgoods, ImagesSpots)
from cssutils import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


# Create your views here.

################## CONT4ENIDO ##################################################################################################

def landing(request):
    return render(request, "akskate/landing.html")

def history(request):

    return render(request, "akskate/history.html")

def practicas(request):

    return render(request, "akskate/good.html")

def partes(request):

    return render(request, "akskate/partes.html")


def motivacion(request):

    return render(request, "akskate/motiv.html")

def subject(request):

    return render(request, "akskate/subjects.html")


################## LOCALIDADES Y SPOTS ##################################################################################################

def spots(request, name_loc):    
    
    loc = Localidad.objects.get(name = name_loc)
    context ={
        "spots" : Spots.objects.filter(localidad=loc),
        
    }
    return render(request, "akskate/spots.html",context)


def park(request, name_park):
    par = Spots.objects.get(name = name_park)
    context = {
        "spot" : par,
        'images': ImagesSpots.objects.all()
    }

    return render(request, "akskate/park.html",  context)



def localidad(request):
    context ={
        "localidades" : Localidad.objects.all()        
    }
    return render(request, "akskate/localidad.html", context)


################## REGISTRO, INICIO Y CIERRE DE SESION ##################################################################################################

def register_view(request):
    """ Registrar usuario"""

    # El usuario alcanzó la ruta a través de POST (al enviar un formulario a través de POST)
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]

        # Asegúrese de que el correo electrónico sea único
        user = User.objects.filter(email=email)
        if len(user) != 0:
            return render(request, "akskate/register.html", {"message": "E-mail ya esta en uso!"})

        #  Asegúrese de que el username sea único
        user = User.objects.filter(username=username)
        if len(user) != 0:
            return render(request, "akskate/register.html", {"message": "Username ya esta en uso!"})
        # Agregar usuario a la base de datos y guardarlo
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )
        user.save()

        return render(request, "akskate/login.html", {"message": "Cuenta creada!"})
    # El usuario alcanzó la ruta a través de GET (como haciendo clic en un enlace o mediante redireccionamiento)
    else:
        return render(request, "akskate/register.html")

  


def loginPague_view(request):
    """ Iniciar sesión de usuario """

    #Si el usuario ya existe, redireccionarlo al index
    if request.user.is_authenticated:
        return redirect('landing')

    else:
        # El usuario alcanzó la ruta a través de POST (al enviar un formulario a través de POST)
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('landing')

            else:
                messages.info(request, "Nombre de usuario o contraseña incorrecta")


        context = {'user':request.user,}
        return render(request, 'akskate/login.html', context)




def logoutUser_view(request):
    logout(request)
    return redirect('landing')


################## STORE ##################################################################################################

def store(request):
    if not request.user.is_authenticated:
        cart = {}
        order = {}

    context = {
        'user': request.user,
        'decks': Decks.objects.all(),
        'trucks': Trucks.objects.all(),
        'wheels': Wheels.objects.all(),
        'bearings': Bearings.objects.all(),
        'hardgoods': Hardgoods.objects.all(),
    }

    if  request.user.is_authenticated:
        try:
            order = Order.objects.get(user=request.user, status="Initiated")

        except:

            order = Order(user=request.user)
            order.save()

        cart = Cart.objects.filter(user=request.user, order_id=order.pk)
        count = 0
    
        for item in cart:
            count += 1
        context["count"] = count

    return render(request, "akskate/store.html", context)


################## CART ##################################################################################################

def add_item_view(request):
    """ Artículo de revisión """

    # Obtener campos de formulario
    name = request.POST["name"]
    item_price = request.POST["item_price"]
    
    # Generar nombre del artículo del carrito
    cart_item = name

    # Iniciar sesión usuario
    user = request.user

    # Obtenga la última orden iniciada
    order = Order.objects.get(user=user, status="Initiated")

    # Obtener ID de pedido
    order_id = order.id

    # Agregue el artículo en el carrito y guárdelo
    cart = Cart(
        user=user,
        order_id=order,
        cart_item=cart_item,
        item_price=item_price,
    )
    cart.save()

    # Incremento total del pedido con precio del artículo
    order.order_total = (order.order_total) + int(item_price)
    
    order.save()

    
    print(order.order_total)

    # Redirigir al usuario para indexar con un mensaje
    messages.success(request, "Artículo agregado!")
    return HttpResponseRedirect(reverse("store"))

def remove_item_view(request):
  

    item_id = request.POST["item_id"]
    item_price = request.POST["item_price"]

    user = request.user

    # Eliminar artículo del carrito
    cart = Cart.objects.filter(id=item_id).delete()

    # Disminuya el total del pedido con el precio del artículo
    order = Order.objects.get(user=user, status="Initiated")
    order.order_total = float(order.order_total) - float(item_price)
    order.save()


    messages.success(request, "Artículo eliminado!")
    return HttpResponseRedirect(reverse("store"))


def cart_view(request):
    """ Muestra el carrito y elimina artículos del carrito """

    # Obtener orden inicializada
    order = Order.objects.get(user=request.user, status="Initiated")

    # Obtén artículos del carrito
    cart = Cart.objects.filter(user=request.user, order_id=order.pk)

    # Contar artículos del carrito
    count = 0
    for item in cart:
        count += 1

    context = {
        "cart": cart,
        "count": count,
        "order_total": order.order_total,
        "order_id": order.id,
    }

    return render(request, "akskate/cart.html", context)


################## pAGO ##################################################################################################

def checkout(request):

    # Obtén orden
    order = Order.objects.get(user=request.user)

    # Obtén artículos del carrito
    cart = Cart.objects.filter(user=request.user, order_id=order.pk)

    # Contar artículos del carrito
    count = 0
    for item in cart:
        count += 1

    context = {
        "cart": cart,
        "count": count,
        "order_total": order.order_total,
        "order_id": order.id,
    }

    if request.method == "POST":
        address = request.POST["address"]
        city = request.POST["city"]
        department = request.POST["department"]

        shipping = ShippingAddress(
            user=request.user,
            order=Order.objects.get(user=request.user),
            address=address,
            city=city,
            department=department,
        )

        print(shipping)
        shipping.save()

    return render(request, "akskate/checkout.html", context)

################## PRODUCTO ##################################################################################################


def show_decks(request,deck):
    madero = Decks.objects.get(name=deck)
    context = {
        'item': madero,
    }
    return render(request, "akskate/show_deck.html", context)


def show_trucks(request,truck):
    eje = Trucks.objects.get(name=truck)
    context = {
        'item': eje,
    }
    return render(request, "akskate/show_truck.html", context)




def show_wheels(request,wheel):
    ruedas = Wheels.objects.get(name=wheel)
    context = {
        'item': ruedas,
    }
    return render(request, "akskate/show_wheel.html", context)


def show_bearings(request,bearing):
    rodamientos = Bearings.objects.get(name=bearing)
    context = {
        'item': rodamientos,
    }
    return render(request, "akskate/show_bearing.html", context)


def show_hardgoods(request,hardgood):
    herr = Hardgoods.objects.get(name=hardgood)
    context = {
        'item': herr,
    }
    return render(request, "akskate/show_hardgood.html", context)