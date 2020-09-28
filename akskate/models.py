from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Localidad(models.Model):
    name = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Spots(models.Model):
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, related_name="local")
    name = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    summary = models.CharField(max_length=255)
    direction = models.CharField(max_length=5000, null=True)
    schedule = models.CharField(max_length=255, null=True)
    chat = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.name}"


class Decks(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField()
    image = models.CharField(max_length=255) #pri_image
    
    def __str__(self):
        return f"{self.name} | {self.price}"



class Wheels(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name} | {self.price}"

class Trucks(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField()
    image = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} | {self.price}"

class Hardgoods(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name} | {self.price}"



class Bearings(models.Model):
    name = models.CharField(max_length=255, null=True)
    price = models.IntegerField()
    image = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name} | {self.price}"


class ImagesSpots(models.Model):
    name = models.CharField(max_length=255, null=True)
    spot = models.ForeignKey(Spots, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.spot}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_total = models.IntegerField(default=0)
    status = models.CharField(max_length=64, default="Initiated")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    # String representation of self
    def __str__(self):
        return f"{self.pk} - {self.user}  |  Status: {self.status}  |  Total: ${self.order_total}  |  Date: {self.date}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart_item = models.CharField(max_length=64)
    item_price = models.IntegerField()

    def __str__(self):
        return f"{self.pk} - {self.user}  |  Order ID: {self.order_id}  |  Item: {self.cart_item}  |  Price: {self.item_price}"



class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
 