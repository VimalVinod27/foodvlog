from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

admin.site.register(Category,CategoryAdmin)
