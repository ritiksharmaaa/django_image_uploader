from django.contrib import admin
from .models import image 

# Register your models here.
@admin.register(image)
class imageAdmin(admin.ModelAdmin):
    list_display = ['id' , 'pic' , 'date']