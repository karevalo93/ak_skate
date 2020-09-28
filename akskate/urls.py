from django.urls import path
from .views import landing
from . import views

urlpatterns = [
    path("", landing, name="landing"),
    path("history", views.history, name="history"),
    path("practicas", views.practicas, name="practicas"),
    path("partes", views.partes, name="partes"),
    path("motivacion", views.motivacion, name="motivacion"),
    path("spots/<str:name_loc>/", views.spots, name = 'spots'),
    path("park/<str:name_park>/", views.park, name = 'park'),
    path("localidad", views.localidad, name="localidad"),
    path("subjects", views.subject, name="subjects"),
    #register,login y logout
    path("register", views.register_view, name="register"),
    path("login", views.loginPague_view, name="login"),
    path("logout", views.logoutUser_view, name="logout"),
    #store
    path("store", views.store, name="store"),
    path("cart", views.cart_view, name="cart"),
    path("add_item", views.add_item_view, name="add_item"),
    path("remove_item", views.remove_item_view, name="remove_item"),
    #path("place_order", views.place_order_view, name="place_order"),
    path("checkout", views.checkout, name="checkout"),
    #showproduct
    path("show_decks/<str:deck>/", views.show_decks, name="show_decks"),
    path("show_trucks/<str:truck>/", views.show_trucks, name="show_trucks"),
    path("show_wheels/<str:wheel>/", views.show_wheels, name="show_wheels"),
    path("show_bearings/<str:bearing>/", views.show_bearings, name="show_bearings"),
    path("show_hardgoods/<str:hardgood>/", views.show_hardgoods, name="show_hardgoods"),
]