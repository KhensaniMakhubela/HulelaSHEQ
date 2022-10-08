from django.contrib import admin
from .models import Category
from .models import Access_status
from .models import MainMenu

# Register your models here.

admin.site.register(Category)
admin.site.register(Access_status)
admin.site.register(MainMenu)

