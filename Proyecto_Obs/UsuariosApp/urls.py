from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from .views import user_list,user_edit,user_delete,user_activate, reset_password,login, error_access,register


urlpatterns = [
    
    # *****  URLS PARA AUTENTICACION DE USUARIOS *******
    path('', RedirectView.as_view(url='login/', permanent=False), name='index'),  # Redirige la raíz a la vista de inicio de sesión
    path('login/', login, name='login'),  # Vista de inicio de sesión
    path('error/', error_access, name='error'),
    path('register/', register, name='register'),
    #path('logout/', user_logout, name='logout'),

    # *****  URLS PARA DASHBOARD PRINICIPAL *******
    #path('api/dash', dash, name='api/dash'),
    

    # *************  URLS PARA  USUARIOS  *******************
    path('api/user', user_list, name='api/user'),
    path('api/user_edit/<int:user_id>/', user_edit, name='api/user_edit'),
    path('api/reset_pwd/<int:user_id>/', reset_password, name='api/reset_pwd'),
    path('api/user_del/<int:user_id>/', user_delete, name='api/user_del'),
    path('api/user_act/<int:user_id>/', user_activate, name='api/user_act'),  
]