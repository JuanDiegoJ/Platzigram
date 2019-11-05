from users.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User

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
    #Crea un bloque para filtrar por los siguientes parámetros
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')
    fieldsets=(
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            ),  
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields' : ('created', 'modified'),
        })
    )
    readonly_fields = ('created', 'modified',)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username',
    'email',
    'first_name',
    'last_name',
    'is_active',
    'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)