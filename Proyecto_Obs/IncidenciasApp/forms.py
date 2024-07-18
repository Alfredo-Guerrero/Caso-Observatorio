from django import forms
from .models import Distritos, Direcciones, Incidencias

class DistritosForm(forms.ModelForm):
    
    class Meta:
            model = Distritos
            fields = [  'PR_IN_IDPK_Dis', 
                        'PR_CH_Nombre_Dis'
                        
                    ]

class DireccionesForm(forms.ModelForm):
    
    class Meta:
            model = Direcciones
            fields = [  'PR_IN_IDPK_Dir', 
                        'PR_CH_Nombre_Dis',
                        'PR_CH_calle',
                        'PR_CH_avenida',
                        'PR_CH_pasaje',
                        'PR_CH_jiron',
                        'PR_CH_zona',
                        'PR_TE_referencia'
                    ]
            
class IncidenciasForm(forms.ModelForm):
    
    class Meta:
            model = Incidencias
            fields = [  'PR_IN_IDPK_Inc', 
                        'PR_CH_Nombre_Dis',
                        'PR_CH_direccion',
                        'PR_CH_categoria',
                        'PR_TE_descripcion',
                        'PR_CH_reportado_por',
                        'PR_DA_fecha',
                        'PR_TI_hora',
                        'PR_IM_foto',
                        'PR_TE_acciones_tomadas'
                    ]



