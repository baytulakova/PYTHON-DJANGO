from django.contrib import admin

from .models import Category
from .models import Client
from .models import Product
from .models import Sale

admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Sale)
