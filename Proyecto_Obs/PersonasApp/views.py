from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Personas
from .forms import PersonasForm
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from .utils import formatear_fecha
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

def reporte_view (request):
    
    return render(request, 'personas/reportes.html')

#   *********************   FUNCION REGISTRAR PERSONAS ***************          
def add_per(request):
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            dni = request.POST.get('dni')
            tipodocumento= request.POST.get('tipodocumento')
            paterno = request.POST.get('paterno')
            materno = request.POST.get('materno')
            nombre = request.POST.get('nombre')
            direccion = request.POST.get('direccion')
            telefono = request.POST.get('telefono')
            correo = request.POST.get('correo')
            sexo = request.POST.get('sexo')
            nacimiento = request.POST.get('nacimiento')

            #tipo_persona = request.POST.get('tipo')

            # Formatear la fecha
            nacimiento_formateada = formatear_fecha(nacimiento)
            
            try:
                persona_existente = Personas.objects.using('personas').get(PR_P_CH_DNI=dni)
                mensaje_error = f"El DNI {dni} de {persona_existente.PR_CH_NOM} {persona_existente.PR_CH_APEPAT} {persona_existente.PR_CH_APEMAT} ya está registrado en el sistema."
                messages.warning(request, mensaje_error)
                return redirect('PersonasApp:api/per_add')
            except ObjectDoesNotExist:
                pass
                
            # Obtener un  objetos que cumpla con las condiciones especificadas


                # Crear una entrada en datos
            entrada = Personas(
                    PR_P_CH_DNI=dni, 
                    PR_CH_TIPODOC= tipodocumento,        
                    PR_CH_APEPAT=paterno,
                    PR_CH_APEMAT=materno,
                    PR_CH_NOM=nombre,
                    PR_CH_DIR=direccion, 
                    PR_CH_TELEF=telefono, 
                    PR_CH_EMAIL=correo,
                    PR_CH_SEXO=sexo,
                    PR_DT_FECNAC=nacimiento_formateada
                    #SERE_chCargo=tipo.per_CH_nomParam
                ) 
            entrada.save(using='personas')                


        # Devolver una respuesta con los datos guardados y redirigir a la ruta deseada
            messages.success(request, 'Registro de Persona grabado correctamente.')
            return redirect('PersonasApp:api/per_add')
        except Exception as e:
            # Manejar cualquier error que pueda ocurrir durante el proceso de guardado
            return JsonResponse({'error': str(e)}, status=500)


    # listado para renderizar a la plantilla
    personas = Personas.objects.using('personas').filter(PR_CH_EST="activo")

    
    # contexto pare renderizar a la plantilla
    contexto = {
        'personas': personas,
    }

    return render(request, 'personas/agregar.html', contexto)


#   ********************* DETALLES  PERSONAS ***************
def get_persona_details(request, dni_per):
    try:
        # Buscar la persona por su DNI
        persona = Personas.objects.using('personas').get(PR_P_CH_DNI=dni_per)

        # Preparar los datos de la persona para enviarlos como JSON
        data = {
            'PR_P_CH_DNI': persona.PR_P_CH_DNI,
            'PR_CH_TIPODOC': persona.PR_CH_TIPODOC,
            'PR_CH_APEPAT': persona.PR_CH_APEPAT,
            'PR_CH_APEMAT': persona.PR_CH_APEMAT,
            'PR_CH_NOM': persona.PR_CH_NOM,
            'PR_CH_DIR': persona.PR_CH_DIR,
            'PR_CH_TELEF': persona.PR_CH_TELEF,
            'PR_CH_EMAIL': persona.PR_CH_EMAIL,
            'PR_CH_SEXO': persona.PR_CH_SEXO,
            'PR_DT_FECNAC': persona.PR_DT_FECNAC,
            
        }

        # Devolver los detalles de la persona como JSON
        return JsonResponse(data)
    except Personas.DoesNotExist:
        # Manejar el caso en el que no se encuentre la persona
        return JsonResponse({'error': 'La persona no existe'}, status=404)
    except Exception as e:
        # Manejar cualquier otro error que pueda ocurrir
        return JsonResponse({'error': str(e)}, status=500)



#   ********************* ACTUALIZAR PERSONAS ***************
def update_per(request, dni_per):
    persona = Personas.objects.using('personas').get(PR_P_CH_DNI=dni_per)

    if request.method == 'POST':
        form = PersonasForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro de Persona actualizado correctamente.')
            return redirect('PersonasApp:api/per_add') 
        else:
            # Obtener el error específico
            error_message = form.errors.as_text()
            messages.error(request, error_message)
    else:
        form = PersonasForm(instance=persona)
        
    return render(request, 'personas/agregar.html', {'form': form, 'persona': persona})

        
#   ********************* ELIMINAR PERSONAS ***************
def del_per(request, per_id):
    try:
        # Obtener el objeto de categoria de persona por su ID utilizando la conexión 'parametros'
        persona  = Personas.objects.using('personas').get(PR_P_CH_DNI=per_id)      
        # Cambiar el estado de la categoria de persona a 'inactivo'
        persona.PR_CH_EST = 'inactivo'
        persona.save()
        # Agregar un mensaje de éxito
        messages.success(request, 'El registro de la Persona se ha eliminado correctamente')
        # Redirigir a la página de lista de cetegoaria de personas después de la eliminación
        return HttpResponseRedirect(reverse('PersonasApp:api/per_add'))
    except Personas.DoesNotExist:
        # Agregar un mensaje de error si la categeria de persona no existe
        messages.error(request, 'Persona no existe en el sistema')
        return HttpResponse('Persona no existe en el sistem', status=404)
    except Exception as e:
        # Agregar un mensaje de error si ocurre algún otro problema durante la eliminación
        messages.error(request, f'Error al eliminar el registro de la Persona: {str(e)}')
        return HttpResponse(f'Error al eliminar el registro de la Persona: {str(e)}', status=500)
    
    












