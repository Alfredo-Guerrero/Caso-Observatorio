document.getElementById('btn-bloquear').addEventListener('click', function() {
    // Obtener todos los checkboxes de serenos seleccionados
    var checkboxes = document.querySelectorAll('.check-sereno:checked');
    var datosSerenos = []; // Array para almacenar los datos de los serenos seleccionados

    // Iterar sobre cada checkbox seleccionado
    checkboxes.forEach(function(checkbox) {
        // Obtener el DNI del sereno del atributo data-dni
        var dni = checkbox.dataset.dni;
        // Obtener el mes de asignación del atributo data-mes
        var mesAsig = checkbox.dataset.mes;

        // Agregar los datos a la lista de serenos
        datosSerenos.push({ dni: dni, mes: mesAsig });
    });

    // Imprimir los datos obtenidos en la consola
    console.log('Datos de los serenos seleccionados:', datosSerenos);

    // Verificar si se seleccionaron checkboxes
    if (datosSerenos.length > 0) {
        // Mostrar una confirmación con SweetAlert
        Swal.fire({
            title: '¿Estás seguro?',
            text: '¿Quieres eliminar las asignaciones seleccionadas?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                // Crear el objeto de datos a enviar al backend
                var data = {
                    dni_serenos: datosSerenos.map(sereno => sereno.dni),
                    mes_asig: datosSerenos[0].mes // Supongo que el mes de todas las asignaciones es el mismo
                };

                // Realizar la solicitud POST al backend
                fetch('/recursoApp/api/asigdel/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            // Si estás utilizando Django, obtén el token CSRF de manera adecuada
                            'X-CSRFToken': getCSRFToken()
                        },
                        body: JSON.stringify(data)
                    })
                    .then(response => response.json())
                    .then(data => {
                        // Manejar la respuesta del backend
                        if (data.success) {
                            // Mostrar un mensaje de éxito con SweetAlert
                            Swal.fire({
                                title: '¡Eliminadas!',
                                text: 'Se eliminaron las asignaciones correctamente.',
                                icon: 'success',
                                confirmButtonColor: '#3085d6',
                                confirmButtonText: 'OK'
                            }).then(() => {
                                // Redireccionar o actualizar la página
                                window.location.reload(); // Actualizar la página
                                // O puedes redirigir a una página específica utilizando:
                                // window.location.href = '/ruta/de/la/pagina.html';
                            });
                        } else {
                            // Mostrar un mensaje de error con SweetAlert
                            Swal.fire({
                                title: 'Error',
                                text: 'Hubo un error al eliminar las asignaciones.',
                                icon: 'error',
                                confirmButtonColor: '#3085d6',
                                confirmButtonText: 'OK'
                            });
                        }
                    })
                    .catch(error => {
                        // Mostrar un mensaje de error si la solicitud falla
                        console.error('Error al realizar la solicitud:', error);
                        // Mostrar un mensaje de error con SweetAlert
                        Swal.fire({
                            title: 'Error',
                            text: 'Hubo un error al realizar la solicitud.',
                            icon: 'error',
                            confirmButtonColor: '#3085d6',
                            confirmButtonText: 'OK'
                        });
                    });
            }
        });
    } else {
        // Si no se seleccionaron checkboxes, mostrar un mensaje con SweetAlert
        Swal.fire({
            title: '¡Alerta!',
            text: 'Por favor, selecciona al menos un sereno para eliminar las asignaciones.',
            icon: 'warning',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'OK'
        });
    }
});

// Función para obtener el token CSRF
function getCSRFToken() {
    var csrfCookie = document.cookie.match(/(^|;) ?csrftoken=([^;]*)(;|$)/);
    return csrfCookie ? csrfCookie[2] : null;
}