from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Complain,Order,OrderUpdate
admin.site.register(Product)
admin.site.register(Complain)
admin.site.register(Order)
admin.site.register(OrderUpdate)

