from django.contrib import admin
from .models import Sobre, Consumo, Beneficios, Depoimentos, Projetos

admin.site.register(Sobre)
admin.site.register(Consumo)
admin.site.register(Beneficios)
admin.site.register(Depoimentos)
admin.site.register(Projetos)

#admin.register(Beneficios)
#class SobreAdmin(admin.ModelAdmin):
    
