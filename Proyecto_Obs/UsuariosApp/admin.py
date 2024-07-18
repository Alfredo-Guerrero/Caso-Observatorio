from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define los campos que deseas mostrar en la lista de usuarios
    list_display = ('username', 'email', 'auth_CH_CodPersonFK', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'auth_CH_CodPersonFK', 'auth_CH_telf', 'auth_CH_telfAlter', 'auth_CH_email_Alter', 'auth_IM_photo')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('username', 'email', 'auth_CH_CodPersonFK')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)