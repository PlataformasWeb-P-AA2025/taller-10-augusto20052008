from django.contrib import admin
from ordenamiento.models import Parroquia, Barrio

# Register your models here.
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'tipo')
    search_fields = ('nombre',)

class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'parroquia')
    list_filter = ('parroquia',)
    raw_id_fields = ('parroquia',)

admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Barrio, BarrioAdmin)
