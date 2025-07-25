from django.contrib import admin
from .models import *

# Register your models here.



class EventAdmin(admin.ModelAdmin):
    list_display = ('id','payload', 'created_at')

admin.site.register(Event,EventAdmin)
    

