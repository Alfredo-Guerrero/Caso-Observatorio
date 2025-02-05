# Generated by Django 5.0.2 on 2024-07-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IncidenciasApp', '0003_alter_direcciones_pr_ch_nombre_dis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidencias',
            fields=[
                ('PR_IN_IDPK_Inc', models.AutoField(primary_key=True, serialize=False)),
                ('PR_CH_Nombre_Dis', models.CharField(blank=True, max_length=100, null=True)),
                ('PR_CH_direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('PR_CH_categoria', models.CharField(blank=True, max_length=30, null=True)),
                ('PR_TE_descripcion', models.TextField(blank=True, null=True)),
                ('PR_CH_reportado_por', models.CharField(blank=True, max_length=100, null=True)),
                ('PR_DA_fecha', models.CharField(blank=True, max_length=22, null=True)),
                ('PR_TI_hora', models.CharField(blank=True, max_length=22, null=True)),
                ('PR_IM_foto', models.ImageField(blank=True, null=True, upload_to='incidencias_fotos/')),
                ('PR_TE_acciones_tomadas', models.TextField(blank=True, null=True)),
                ('PR_CH_EST', models.CharField(default='activo', max_length=10)),
            ],
            options={
                'db_table': 'Incidencias',
            },
        ),
    ]
