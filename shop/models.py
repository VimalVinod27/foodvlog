from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    img=models.ImageField(upload_to='pictures')
    price=models.IntegerField()
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    def get_url(self):
        return reverse('shop:shop_detail',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('shop:shop_category',args=[self.slug])

