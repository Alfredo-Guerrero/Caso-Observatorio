from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Distritos, Direcciones, Incidencias
from .forms import DistritosForm, DireccionesForm, IncidenciasForm
from django.http import JsonResponse
#from django.core.exceptions import ValidationError
#from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from .utils import formatear_fecha, formatear_hora
from django.db.models import Count
import json


def dash(request):
    # Obtén el mensaje de bienvenida de la sesión
    welcome_message = request.session.get('welcome_message')

    # Si el mensaje de bienvenida existe, elimínalo de la sesión
    if welcome_message is not None:
        del request.session['welcome_message']

    # Crear el contexto
    context = {
        'username': request.user.username,
        'welcome_message': welcome_message,
    }

    # Renderiza la plantilla con el contexto
    return render(request, 'escritorio/dash.html', context)


#   *********************   FUNCION REGISTRAR DISTRITOS ***************          
def add_dis(request):
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            id = request.POST.get('id')
            nombredistrito= request.POST.get('nombredistrito')
            

            try:
                distrito_existente = Distritos.objects.using('distritos').get(PR_IN_IDPK_Dis=id)
                mensaje_error = f"La ID {id} de {distrito_existente.PR_CH_Nombre_Dis} ya está registrado en el sistema."
                messages.warning(request, mensaje_error)
                return redirect('IncidenciasApp:api/dis_add')
            except ObjectDoesNotExist:
                pass
                
            # Obtener un  objetos que cumpla con las condiciones especificadas

                # Crear una entrada en datos
            entrada = Distritos(
                    PR_IN_IDPK_Dis=id, 
                    PR_CH_Nombre_Dis= nombredistrito,        
                    
                ) 
            entrada.save(using='distritos')                


        # Devolver una respuesta con los datos guardados y redirigir a la ruta deseada
            messages.success(request, 'Registro de Distrito grabado correctamente.')
            return redirect('IncidenciasApp:api/dis_add')
        except Exception as e:
            # Manejar cualquier error que pueda ocurrir durante el proceso de guardado
            return JsonResponse({'error': str(e)}, status=500)


    # listado para renderizar a la plantilla
    distritos = Distritos.objects.using('distritos').filter(PR_CH_EST="activo")

    
    # contexto pare renderizar a la plantilla
    contexto = {
        'distritos': distritos,
    }

    return render(request, 'distritos/agregar.html', contexto)


#   ********************* DETALLES  Distritos ***************
def get_distrito_details(request, id_dis):
    try:
        # Buscar la persona por su DNI
        persona = Distritos.objects.using('distritos').get(PR_IN_IDPK_Dis=id_dis)

        # Preparar los datos de la persona para enviarlos como JSON
        data = {
            'PR_IN_IDPK_Dis': persona.PR_IN_IDPK_Dis,
            'PR_CH_Nombre_Dis': persona.PR_CH_Nombre_Dis,
            
        }

        # Devolver los detalles de la persona como JSON
        return JsonResponse(data)
    except Distritos.DoesNotExist:
        # Manejar el caso en el que no se encuentre el distrito
        return JsonResponse({'error': 'El distrito no existe'}, status=404)
    except Exception as e:
        # Manejar cualquier otro error que pueda ocurrir
        return JsonResponse({'error': str(e)}, status=500)



#   ********************* ACTUALIZAR DISTRITOS ***************
def update_dis(request, id_dis):
    distrito = Distritos.objects.using('distritos').get(PR_IN_IDPK_Dis=id_dis)

    if request.method == 'POST':
        form = DistritosForm(request.POST, instance=distrito)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de Distrito actualizado correctamente.')
            return redirect('IncidenciasApp:api/dis_add') 
        else:
            # Obtener el error específico
            error_message = form.errors.as_text()
            messages.error(request, error_message)
    else:
        form = DistritosForm(instance=distrito)
        
    return render(request, 'distritos/agregar.html', {'form': form, 'distrito': distrito})

        
#   ********************* ELIMINAR DISTRITOS ***************
def del_dis(request, dis_id):
    try:
        # Obtener el objeto de categoria de distrito por su ID utilizando la conexión 'parametros'
        distrito  = Distritos.objects.using('distritos').get(PR_IN_IDPK_Dis=dis_id)      
        # Cambiar el estado de la categoria de distrito a 'inactivo'
        distrito.PR_CH_EST = 'inactivo'
        distrito.save()
        # Agregar un mensaje de éxito
        messages.success(request, 'El registro del Distrito se ha eliminado correctamente')
        # Redirigir a la página de lista de cetegoaria de distritos después de la eliminación
        return HttpResponseRedirect(reverse('IncidenciasApp:api/dis_add'))
    except Distritos.DoesNotExist:
        # Agregar un mensaje de error si la categeria de distrito no existe
        messages.error(request, 'Distrito no existe en el sistema')
        return HttpResponse('Distrito no existe en el sistem', status=404)
    except Exception as e:
        # Agregar un mensaje de error si ocurre algún otro problema durante la eliminación
        messages.error(request, f'Error al eliminar el registro del Distrito: {str(e)}')
        return HttpResponse(f'Error al eliminar el registro del Distrito: {str(e)}', status=500)
    
############################################################################################################

#   *********************   FUNCION REGISTRAR DIRECCIONES ***************          
def add_dir(request):
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            id = request.POST.get('id')
            nombredistrito= request.POST.get('distrito')
            calle= request.POST.get('calle')
            avenida= request.POST.get('avenida')
            pasaje= request.POST.get('pasaje')
            jiron= request.POST.get('jiron')
            zona= request.POST.get('zona')
            referencia= request.POST.get('referencia')
            
            try:
                direccion_existente = Direcciones.objects.using('distritos').get(PR_IN_IDPK_Dir=id)
                mensaje_error = f"La ID {id} de {direccion_existente.PR_CH_Nombre_Dis} {direccion_existente.PR_CH_calle} {direccion_existente.PR_CH_avenida} {direccion_existente.PR_CH_pasaje} {direccion_existente.PR_CH_jiron} {direccion_existente.PR_CH_zona} ya está registrado en el sistema."
                messages.warning(request, mensaje_error)
                return redirect('IncidenciasApp:api/dir_add')
            except ObjectDoesNotExist:
                pass
                
            # Obtener un  objetos que cumpla con las condiciones especificadas
            distritos = Distritos.objects.using('distritos').get(PR_CH_Nombre_Dis=nombredistrito)
            
            
                # Crear una entrada en datos
            entrada = Direcciones(
                    PR_IN_IDPK_Dir=id, 
                    PR_CH_Nombre_Dis= distritos.PR_CH_Nombre_Dis,
                    PR_CH_calle = calle,
                    PR_CH_avenida = avenida, 
                    PR_CH_pasaje = pasaje,
                    PR_CH_jiron = jiron,
                    PR_CH_zona = zona,
                    PR_TE_referencia = referencia
                ) 
            entrada.save(using='distritos')                


        # Devolver una respuesta con los datos guardados y redirigir a la ruta deseada
            messages.success(request, 'Registro de Direcciones grabado correctamente.')
            return redirect('IncidenciasApp:api/dir_add')
        except Exception as e:
            # Manejar cualquier error que pueda ocurrir durante el proceso de guardado
            return JsonResponse({'error': str(e)}, status=500)


    # listado para renderizar a la plantilla
    direcciones = Direcciones.objects.using('distritos').filter(PR_CH_EST="activo")
    distritos = Distritos.objects.using('distritos').filter( PR_CH_EST="activo")
    
    
    # contexto pare renderizar a la plantilla
    contexto = {
        'direcciones': direcciones,
        'distritos': distritos,
    }

    return render(request, 'direcciones/agregar.html', contexto)


#   ********************* DETALLES  DIRECCIONES ***************
def get_direccion_details(request, id_dir):
    try:
        # Buscar la persona por su DNI
        direccion = Direcciones.objects.using('distritos').get(PR_IN_IDPK_Dir=id_dir)

        # Preparar los datos de la persona para enviarlos como JSON
        data = {
            'PR_IN_IDPK_Dir': direccion.PR_IN_IDPK_Dir,
            'PR_CH_Nombre_Dis': direccion.PR_CH_Nombre_Dis,
            'PR_CH_calle': direccion.PR_CH_calle,
            'PR_CH_avenida': direccion.PR_CH_avenida,
            'PR_CH_pasaje': direccion.PR_CH_pasaje,
            'PR_CH_jiron': direccion.PR_CH_jiron,
            'PR_CH_zona': direccion.PR_CH_zona,
            'PR_TE_referencia': direccion.PR_TE_referencia
        }

        # Devolver los detalles de la persona como JSON
        return JsonResponse(data)
    except Direcciones.DoesNotExist:
        # Manejar el caso en el que no se encuentre el distrito
        return JsonResponse({'error': 'La Direccion no existe'}, status=404)
    except Exception as e:
        # Manejar cualquier otro error que pueda ocurrir
        return JsonResponse({'error': str(e)}, status=500)



#   ********************* ACTUALIZAR DIRECCIONES ***************
def update_dir(request, id_dir):
    direccion = Direcciones.objects.using('distritos').get(PR_IN_IDPK_Dir=id_dir)

    if request.method == 'POST':
        form = DireccionesForm(request.POST, instance=direccion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de Direccion actualizado correctamente.')
            return redirect('IncidenciasApp:api/dir_add') 
        else:
            # Obtener el error específico
            error_message = form.errors.as_text()
            messages.error(request, error_message)
    else:
        form = DireccionesForm(instance=direccion)
        
    return render(request, 'direcciones/agregar.html', {'form': form, 'direccion': direccion})

        
#   ********************* ELIMINAR DIRECCIONES ***************
def del_dir(request, dir_id):
    try:
        # Obtener el objeto de categoria de distrito por su ID utilizando la conexión 'parametros'
        direccion  = Direcciones.objects.using('distritos').get(PR_IN_IDPK_Dir=dir_id)      
        # Cambiar el estado de la categoria de distrito a 'inactivo'
        direccion.PR_CH_EST = 'inactivo'
        direccion.save()
        # Agregar un mensaje de éxito
        messages.success(request, 'El registro del Direccion se ha eliminado correctamente')
        # Redirigir a la página de lista de cetegoaria de distritos después de la eliminación
        return HttpResponseRedirect(reverse('IncidenciasApp:api/dir_add'))
    except Direcciones.DoesNotExist:
        # Agregar un mensaje de error si la categeria de Direccion no existe
        messages.error(request, 'Direccion no existe en el sistema')
        return HttpResponse('Direccion no existe en el sistem', status=404)
    except Exception as e:
        # Agregar un mensaje de error si ocurre algún otro problema durante la eliminación
        messages.error(request, f'Error al eliminar el registro de Direccion: {str(e)}')
        return HttpResponse(f'Error al eliminar el registro del Direccion: {str(e)}', status=500)
    
############################################################################################################

#   *********************   FUNCION REGISTRAR INCIDENCIAS ***************          
def add_inc(request):
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            id = request.POST.get('id')
            nombredistrito = request.POST.get('distrito')
            direccion = request.POST.get('direccion')
            categoria = request.POST.get('categoria')
            descripcion = request.POST.get('descripcion')
            reportado = request.POST.get('reportado')
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')
            foto = request.FILES.get('foto')
            acciontomada = request.POST.get('acciontomada')
            
            # Validar y formatear la fecha y hora si existen
            if fecha:
                fecha = formatear_fecha(fecha)
            if hora:
                hora = formatear_hora(hora)
            
            try:
                # Verificar si ya existe una incidencia con el mismo ID
                incidencia_existente = Incidencias.objects.using('distritos').get(PR_IN_IDPK_Inc=id)
                mensaje_error = f"La ID {id} de {incidencia_existente.PR_CH_Nombre_Dis} ya está registrada en el sistema."
                messages.warning(request, mensaje_error)
                return redirect('IncidenciasApp:api/inc_add')
            except ObjectDoesNotExist:
                # Si no existe, proceder a crear una nueva incidencia
                distrito = Distritos.objects.using('distritos').get(PR_CH_Nombre_Dis=nombredistrito)
                nueva_incidencia = Incidencias(
                    PR_IN_IDPK_Inc=id,
                    PR_CH_Nombre_Dis=distrito.PR_CH_Nombre_Dis,
                    PR_CH_direccion=direccion,
                    PR_CH_categoria=categoria,
                    PR_TE_descripcion=descripcion,
                    PR_CH_reportado_por=reportado,
                    PR_DA_fecha=fecha,
                    PR_TI_hora=hora,
                    PR_IM_foto=foto,
                    PR_TE_acciones_tomadas=acciontomada
                )
                nueva_incidencia.save(using='distritos')

                messages.success(request, 'Registro de Incidencia grabado correctamente.')
                return redirect('IncidenciasApp:api/inc_add')
        
        except Exception as e:
            # Manejar cualquier otro error que pueda ocurrir
            return JsonResponse({'error': str(e)}, status=500)

    # Obtener listas para renderizar la plantilla
    direcciones = Direcciones.objects.using('distritos').filter(PR_CH_EST="activo")
    distritos = Distritos.objects.using('distritos').filter(PR_CH_EST="activo")
    incidencias = Incidencias.objects.using('distritos').filter(PR_CH_EST="activo")
    
    # Contexto para renderizar la plantilla
    contexto = {
        'direcciones': direcciones,
        'distritos': distritos,
        'incidencias': incidencias,
    }

    return render(request, 'incidencias/agregar.html', contexto)

#   ********************* DETALLES  INCIDENCIA ***************
def get_incidencia_details(request, id_inc):
    try:
        # Buscar la persona por su DNI
        incidencia = Incidencias.objects.using('distritos').get(PR_IN_IDPK_Inc=id_inc)

        # Preparar los datos de la persona para enviarlos como JSON
        data = {
            'PR_IN_IDPK_Inc': incidencia.PR_IN_IDPK_Inc,
            'PR_CH_Nombre_Dis': incidencia.PR_CH_Nombre_Dis,
            'PR_CH_direccion': incidencia.PR_CH_direccion,
            'PR_CH_categoria': incidencia.PR_CH_categoria,
            'PR_TE_descripcion': incidencia.PR_TE_descripcion,
            'PR_CH_reportado_por': incidencia.PR_CH_reportado_por,
            'PR_DA_fecha': incidencia.PR_DA_fecha,
            'PR_TI_hora': incidencia.PR_TI_hora,
            'PR_IM_foto': incidencia.PR_IM_foto,
            'PR_TE_acciones_tomadas': incidencia.PR_TE_acciones_tomadas
        }

        # Devolver los detalles de la persona como JSON
        return JsonResponse(data)
    except Incidencias.DoesNotExist:
        # Manejar el caso en el que no se encuentre la inicdencia
        return JsonResponse({'error': 'La Incidencia no existe'}, status=404)
    except Exception as e:
        # Manejar cualquier otro error que pueda ocurrir
        return JsonResponse({'error': str(e)}, status=500)



#   ********************* ACTUALIZAR INCIDENCIA ***************
def update_inc(request, id_inc):
    incidencia = Incidencias.objects.using('distritos').get(PR_IN_IDPK_Inc=id_inc)

    if request.method == 'POST':
        form = IncidenciasForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de Direccion actualizado correctamente.')
            return redirect('IncidenciasApp:api/inc_add') 
        else:
            # Obtener el error específico
            error_message = form.errors.as_text()
            messages.error(request, error_message)
    else:
        form = IncidenciasForm(instance=incidencia)
        
    return render(request, 'incidencias/agregar.html', {'form': form, 'incidencia': incidencia})

        
#   ********************* ELIMINAR INCIDENCIAS ***************
def del_inc(request, inc_id):
    try:
        # Obtener el objeto de categoria de distrito por su ID utilizando la conexión 'parametros'
        incidencia  = Incidencias.objects.using('distritos').get(PR_IN_IDPK_Inc=inc_id)      
        # Cambiar el estado de la categoria de Incidencia a 'inactivo'
        incidencia.PR_CH_EST = 'inactivo'
        incidencia.save()
        # Agregar un mensaje de éxito
        messages.success(request, 'El registro del Incidencia se ha eliminado correctamente')
        # Redirigir a la página de lista de cetegoaria de Incidencia después de la eliminación
        return HttpResponseRedirect(reverse('IncidenciasApp:api/inc_add'))
    except Incidencias.DoesNotExist:
        # Agregar un mensaje de error si la categeria de Incidencia no existe
        messages.error(request, 'Incidencia no existe en el sistema')
        return HttpResponse('Incidencia no existe en el sistem', status=404)
    except Exception as e:
        # Agregar un mensaje de error si ocurre algún otro problema durante la eliminación
        messages.error(request, f'Error al eliminar el registro de Incidencia: {str(e)}')
        return HttpResponse(f'Error al eliminar el registro de Incidencia: {str(e)}', status=500)
    
    
def reporte_view (request):
    
    return render(request, 'incidencias/reportes.html')












