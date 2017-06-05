from django.contrib import admin

from .models import Article
from .models import Image
from .models import News

admin.site.register(Article)
admin.site.register(Image)
admin.site.register(News)
