from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from .views import dash, add_per,get_persona_details, update_per,del_per, reporte_view


urlpatterns = [

    # *************  URLS PARA DASHBOARD PRINICIPAL *******************
    path('api/dash', dash, name='api/dash'),
    
    # *************  URLS PARA PERSONAS ******************* 
    path('api/per_add', add_per, name='api/per_add'),
    path('api/per_detail/<str:dni_per>/', get_persona_details, name='api_per_detail'),
    path('api/per_update/<str:dni_per>/', update_per, name='api_per_update'),
    path('api/per_del/<str:per_id>/', del_per, name='api/per_del'),
    
    # Nueva URL para el dashboard con el gráfico
    path('reporte/', reporte_view, name='reporte'),
    
]