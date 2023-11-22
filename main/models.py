from django.db import models
from django.contrib.auth.models import User

class person(models.Model):
    display_name = models.CharField(max_length=30)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
# Create your models here.
class BarangWishlist(models.Model):
    owner = models.ForeignKey(person, on_delete=models.CASCADE)
    harga_barang = models.IntegerField()
