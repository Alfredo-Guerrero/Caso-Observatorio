from django import forms
from .models import Personas

class PersonasForm(forms.ModelForm):
    
    class Meta:
            model = Personas
            fields = [  'PR_P_CH_DNI', 
                        'PR_CH_TIPODOC', 
                        'PR_CH_APEPAT', 
                        'PR_CH_APEMAT', 
                        'PR_CH_NOM', 
                        'PR_CH_DIR', 
                        'PR_CH_TELEF', 
                        'PR_CH_EMAIL',  
                        'PR_CH_SEXO',
                        'PR_DT_FECNAC'
                    ]




