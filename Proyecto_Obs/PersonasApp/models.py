from django.db import models

# Create your models here.

class Personas(models.Model):
    PR_P_CH_DNI = models.CharField(max_length=15, primary_key=True)
    PR_CH_TIPODOC = models.CharField(max_length=25, blank=True, null=True)
    PR_CH_APEPAT = models.CharField(max_length=50, blank=True, null=True)
    PR_CH_APEMAT = models.CharField(max_length=50, blank=True, null=True)
    PR_CH_NOM = models.CharField(max_length=50, blank=True, null=True)
    PR_CH_DIR = models.CharField(max_length=450, blank=True, null=True)
    PR_CH_TELEF = models.CharField(max_length=50, blank=True, null=True)
    PR_CH_EMAIL = models.CharField(max_length=125, blank=True, null=True)
    PR_CH_SEXO = models.CharField(max_length=1, blank=True, null=True)
    PR_DT_FECNAC = models.CharField(max_length=20, blank=True, null=True)
    PR_CH_EST = models.CharField(max_length=10,default='activo')
    
    def __str__(self):
        return self.PR_P_CH_DNI
    
    class Meta:
        
        db_table = 'Personas'
        app_label = 'PersonasApp'


