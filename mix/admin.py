from django.contrib import admin
from .models import Car

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name','description','image_admin')
    readonly_fields = ('image_admin',)
    
admin.site.register(Produto, ProdutoAdmin)