from django.db import models
from shop.models import *
# Create your models here.
class Cart_list(models.Model):
    cart_user_id=models.CharField(max_length=200,unique=True)

    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_user_id

class Cart_items(models.Model):
    cart=models.ForeignKey(Cart_list,on_delete=models.CASCADE)
    prodt=models.ForeignKey(Product,on_delete=models.CASCADE)
    quant=models.IntegerField()

    def __str__(self):
        return self.cart.cart_user_id

    def sub_total(self):
        total=self.quant*self.prodt.price
        return total





