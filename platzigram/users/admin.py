from users.models import Profile
from django.contrib import admin

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #Muestra una lista de usuarios con los siguientes campos
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    #Muestra una lista de usuarios con estos campos y tienen un link
    #para editar el usuario
    list_display_links = ('pk', 'picture')
    #Permite que se pueda editar el usuario desde la lista de usuarios
    list_editable = ('phone_number', 'website')
    #Crea una barra de búsqueda con los siguientes parametros
    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name',
    'phone_number')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')