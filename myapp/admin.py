from django.contrib import admin
from .models import Fruit
# Register your models here.
class FruitAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_filter=('name','price',)
    list_display=('name',)
admin.site.register(Fruit,FruitAdmin)    