from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from PersonasApp.models import Personas
from .forms import UserForm, UserConfigForm, ResetPasswordForm
from UsuariosApp.models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout

 # ************* CREAR  USUARIOS POR CONSOLA *******************

def login (request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        custom_user = authenticate(request, username=username, password=password)
        
        if custom_user is not None:
            if custom_user.is_active:
                auth_login(request, custom_user)
                messages.success(request, 'Has iniciado sesión correctamente.')
                request.session['welcome_message'] = f'Bienvenido, {username}!'
                return redirect('PersonasApp:api/dash')
            else:
                messages.error(request, 'Tu cuenta está desactivada. No tienes acceso.')
                return redirect('UsuariosApp:error')  # Redirige a la página de error de acceso si la cuenta está desactivada
        else:
            # Aquí manejamos explícitamente el caso en que el usuario existe pero la cuenta está inactiva
            if CustomUser.objects.filter(username=username).exists():
                return redirect(reverse('UsuariosApp:error'))
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            return render(request, 'escritorio/login.html')
    else:
        # Eliminar la variable de sesión welcome_message si existe
        if 'welcome_message' in request.session:
            del request.session['welcome_message']
    
    
    return render(request, 'escritorio/login.html')

def error_access(request):
    return render(request, 'escritorio/error_acces.html')

def register (request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Establecer la contraseña
            user.is_active = True  # Asegúrate de que el usuario esté activo
            user.save()
            messages.success(request, '¡El usuario se ha registrado exitosamente!')
            return redirect('login')  # Redirige al login después de registrar
        else:
            messages.error(request, '¡Error al registrar el usuario!')
    else:
        form = UserForm()

    return render(request, 'escritorio/register.html', {'form': form})
    

 # ************* LISTAR Y CREAR Y USUARIOS  *******************
def user_list(request):
    try:
        if request.method == 'POST':
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                sereno_cod = form.cleaned_data['dni']
                password = form.cleaned_data['password']
                
                # Verifica si ya existe un usuario asociado al código de trabajador
                if CustomUser.objects.filter(auth_CH_CodPersonFK=sereno_cod).exists():
                    messages.error(request, '¡Ya existe un usuario asociado a este código de trabajador!')
                else:
                    try:
                        # Obtener información del trabajador
                        sereno = Personas.objects.using('personas').get(PR_P_CH_DNI=sereno_cod)
                        # Generar el username a partir del trabajador
                        username = (sereno.PR_CH_APEPAT[0] + sereno.PR_CH_APEMAT + sereno.PR_CH_NOM[0] + sereno_cod[-2:]).upper()
                        # Crear el usuario y guardar
                        user = form.save(commit=False)
                        user.username = username.upper()
                        user.set_password(password)
                        user.is_active = True
                        user.auth_CH_CodPersonFK = sereno_cod  # Guardar el código de trabajador asociado
                        user.save()
                        messages.success(request, '¡El usuario se ha agregado exitosamente!')
                    except Personas.DoesNotExist:
                        messages.error(request, 'No se encontró un sereno con el DNI proporcionado.')
                return redirect('UsuariosApp:api/user')
            else:
                messages.error(request, '¡Error al agregar el usuario!')
        else:
            form = UserForm()

        # Obtener todos los usuarios y sus datos de trabajador asociados
        usuarios = CustomUser.objects.all()
        usuarios_con_sereno = []
        for usuario in usuarios:
            # Verificar si el usuario fue creado a través del código de Sereno
            if usuario.auth_CH_CodPersonFK:
                try:
                    # Obtener información del trabajador asociado
                    sereno = Personas.objects.using('personas').get(PR_P_CH_DNI=usuario.auth_CH_CodPersonFK)
                    nombre_completo = f"{sereno.PR_CH_APEPAT} {sereno.PR_CH_APEMAT} {sereno.PR_CH_NOM}"
                except Personas.DoesNotExist:
                    nombre_completo = ""
            else:
                # Si el usuario es un superusuario, dejar el nombre vacío
                nombre_completo = ""

            usuarios_con_sereno.append({'usuario': usuario, 'nombre_completo': nombre_completo})

        # Obtener todos los Serenos disponibles
        serenos = Personas.objects.using('personas').all()

        return render(request, 'usuarios/index.html', {
            'form': form,
            'usuarios': usuarios_con_sereno,
            'serenos': serenos,
        })

    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
        return redirect('UsuariosApp:api/user')

 # *************  EDITAR USUARIOS  *******************
def user_edit(request, user_id):
    usuario = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = UserConfigForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, '¡El usuario se ha actualizado exitosamente!')
            return redirect('UsuariosApp:api/user')  # Redirige a la lista de usuarios
        else:
            # Obtener el error específico
            error_message = form.errors.as_text()
            messages.error(request, error_message)
    else:
        form = UserConfigForm(instance=usuario)
        
    return render(request, 'usuarios/index.html', {'form': form, 'usuario': usuario})


def reset_password(request, user_id):
    usuario = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST, instance=usuario)
        if form.is_valid():
            # Accede al campo confirm_password en lugar de password
            password = form.cleaned_data['confirm_password']
            # Utiliza set_password para encriptar la contraseña
            usuario.set_password(password)
            usuario.save()  # Guarda el usuario actualizado
            messages.success(request, '¡La contraseña ha sido restablecida exitosamente!')
            return redirect('UsuariosApp:api/user')
        else:
            error_message = form.errors.as_text()
            messages.error(request, error_message)
    else:
        form = ResetPasswordForm(instance=usuario)
        
    return render(request, 'usuarios/index.html', {'form': form, 'usuario': usuario})


 # *************  DESACTIVAR USUARIOS  *******************
def user_delete(request, user_id):
    try:
        # Obtener el objeto Usuario por su ID 
        usuario = CustomUser.objects.get(id =user_id)
        
        # Cambiar el estado del usuario a 'inactivo'
        usuario.is_active = False
        usuario.save()

        # Agregar un mensaje de éxito
        messages.success(request, 'El Usuario se ha desactivado correctamente')

        # Redirigir a la página de lista de usuarios después de la desactivacion
        return HttpResponseRedirect(reverse('UsuariosApp:api/user'))
    except User.DoesNotExist:
        # Agregar un mensaje de error si el usuario no existe
        messages.error(request, 'El Usuario no existe')
        return HttpResponse('El Usuario no existe', status=404)
    except Exception as e:
        # Agregar un mensaje de error si ocurre algún otro problema durante la eliminación
        messages.error(request, f'Error al eliminar el Usuario: {str(e)}')
        return HttpResponse(f'Error al eliminar el usuario: {str(e)}', status=500)


 # *************  ACTIVAR USUARIOS  ******************* 
def user_activate(request, user_id):
    try:
        # Obtener el objeto Usuario por su ID 
        usuario = CustomUser.objects.get(id =user_id)
        
        # Cambiar el estado del usuario a 'inactivo'
        usuario.is_active = True
        usuario.save()

        # Agregar un mensaje de éxito
        messages.success(request, 'Se activo el Usuario correctamente')

        # Redirigir a la página de lista de usuarios después de la desactivacion
        return HttpResponseRedirect(reverse('UsuariosApp:api/user'))
    except User.DoesNotExist:
        # Agregar un mensaje de error si el usuario no existe
        messages.error(request, 'El Usuario no existe')
        return HttpResponse('El Usuario no existe', status=404)
    except Exception as e:
        # Agregar un mensaje de error si ocurre algún otro problema durante la eliminación
        messages.error(request, f'Error al activar el Usuario: {str(e)}')
        return HttpResponse(f'Error al activar el usuario: {str(e)}', status=500)
