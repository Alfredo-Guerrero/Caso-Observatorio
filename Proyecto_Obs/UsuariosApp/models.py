from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    auth_CH_CodPersonFK = models.CharField(max_length=15, blank=True, null=True)
    auth_CH_telf = models.CharField(max_length=9, blank=True, null=True)
    auth_CH_telfAlter = models.CharField(max_length=9, blank=True, null=True)
    auth_CH_email_Alter = models.CharField(max_length=255, blank=True, null=True)
    auth_IM_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    groups = models.ManyToManyField('auth.Group', related_name='customuser_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_user_permissions')
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'auth_usuarios'

