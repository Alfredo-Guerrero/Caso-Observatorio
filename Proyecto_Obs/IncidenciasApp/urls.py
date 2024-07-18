from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from .views import dash, add_dis, get_distrito_details, update_dis, del_dis, add_dir, get_direccion_details, update_dir, del_dir, add_inc, get_incidencia_details, update_inc, del_inc, reporte_view


urlpatterns = [

    # *************  URLS PARA DASHBOARD PRINICIPAL *******************
    path('api/dash', dash, name='api/dash'),
    
    # *************  URLS PARA DISTRITOS ******************* 
    path('api/dis_add', add_dis, name='api/dis_add'),
    path('api/dis_detail/<int:id_dis>/', get_distrito_details, name='api_dis_detail'),
    path('api/dis_update/<int:id_dis>/', update_dis, name='api_dis_update'),
    path('api/dis_del/<int:dis_id>/', del_dis, name='api/dis_del'),
    
     # *************  URLS PARA DIRECCIONES ******************* 
    path('api/dir_add', add_dir, name='api/dir_add'),
    path('api/dir_detail/<int:id_dir>/', get_direccion_details, name='api_dir_detail'),
    path('api/dir_update/<int:id_dir>/', update_dir, name='api_dir_update'),
    path('api/dir_del/<int:dir_id>/', del_dir, name='api/dir_del'),
    
     # *************  URLS PARA INCIDENCIAS ******************* 
    path('api/inc_add', add_inc, name='api/inc_add'),
    path('api/inc_detail/<int:id_inc>/', get_incidencia_details, name='api_inc_detail'),
    path('api/inc_update/<int:id_inc>/', update_inc, name='api_inc_update'),
    path('api/inc_del/<int:inc_id>/', del_inc, name='api/inc_del'),
    
    # Nueva URL para el dashboard con el gráfico
    path('reporte/', reporte_view, name='reporte'),
    
]