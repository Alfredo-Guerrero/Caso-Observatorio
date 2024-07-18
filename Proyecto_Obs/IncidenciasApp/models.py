from django.db import models
import uuid
# Create your models here.

class Distritos(models.Model):
    
    PR_IN_IDPK_Dis = models.AutoField(primary_key=True)
    PR_CH_Nombre_Dis = models.CharField(max_length=50, blank=True, null=True)
    PR_CH_EST = models.CharField(max_length=10,default='activo')
    
    def __str__(self):
        return self.PR_CH_Nombre_Dis
    
    class Meta:
        
        db_table = 'Distritos'
        app_label = 'IncidenciasApp'
        
class Direcciones(models.Model):
    PR_IN_IDPK_Dir = models.AutoField(primary_key=True)
    PR_CH_Nombre_Dis = models.CharField(max_length=100, blank=True, null=True)
    PR_CH_calle = models.CharField(max_length=100, blank=True, null=True)
    PR_CH_avenida = models.CharField(max_length=100, blank=True, null=True)
    PR_CH_pasaje = models.CharField(max_length=100, blank=True, null=True)
    PR_CH_jiron = models.CharField(max_length=100, blank=True, null=True)
    PR_CH_zona = models.CharField(max_length=100, blank=True, null=True)
    PR_TE_referencia = models.TextField(blank=True, null=True)
    PR_CH_EST = models.CharField(max_length=10, default='activo')

    def __str__(self):
        return self.PR_CH_Nombre_Dis
    
    class Meta:
        db_table = 'Direcciones'
        app_label = 'IncidenciasApp'
        
class Incidencias(models.Model):
    PR_IN_IDPK_Inc = models.AutoField(primary_key=True)
    PR_CH_Nombre_Dis = models.CharField(max_length=100, blank=True, null=True)
    PR_CH_direccion = models.CharField(max_length=100, blank=True, null=True)
    PR_CH_categoria = models.CharField(max_length=30, blank=True, null=True)
    PR_TE_descripcion = models.TextField(blank=True, null=True)
    PR_CH_reportado_por = models.CharField(max_length=100, blank=True, null=True)
    PR_DA_fecha = models.CharField(max_length=22, blank=True, null=True)
    PR_TI_hora = models.CharField(max_length=22, blank=True, null=True)
    PR_IM_foto = models.ImageField(upload_to='incidencias_fotos/', blank=True, null=True)
    PR_TE_acciones_tomadas = models.TextField(blank=True, null=True)
    PR_CH_EST = models.CharField(max_length=10, default='activo')

    def __str__(self):
        return self.PR_CH_direccion

    class Meta:
        db_table = 'Incidencias'
        managed = False
        app_label = 'IncidenciasApp'

