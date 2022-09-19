from django.contrib import admin
from .models import TblClients, TblSites, TblSystem
# Register your models here.

admin.site.register(TblClients)
admin.site.register(TblSites)
admin.site.register(TblSystem)