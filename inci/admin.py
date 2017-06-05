from django.contrib import admin

from .models import Brand
from .models import Category
from .models import Certification
from .models import Ingredient
from .models import Product
from .models import Type

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Certification)
admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(Type)
