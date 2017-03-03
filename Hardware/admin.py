from django.contrib import admin
from models import *

class HardwareAdmin(admin.ModelAdmin):
    list_display = ['hdName','hdCode','hdDesc','hdType']

admin.site.register(Hardware,HardwareAdmin)

# Register your models here.