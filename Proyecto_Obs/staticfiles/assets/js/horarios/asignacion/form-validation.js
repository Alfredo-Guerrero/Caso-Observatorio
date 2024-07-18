// Función para validar antes de enviar el formulario
function validarAntesDeEnviar() {
    var mesSeleccionado = document.getElementById("mes").value;
    var anioSeleccionado = document.getElementById("anio").value;
    var dniSeleccionado = document.getElementById("dni").value;

    // Verificar si el mes, el año y el DNI del sereno están seleccionados
    if (mesSeleccionado && anioSeleccionado && dniSeleccionado) {
        // Verificar si el DNI ya ha sido seleccionado para el mes y año seleccionados
        var dniRepetido = asignacionesPorSereno.some(function(asignacion) {
            return asignacion.mes === mesSeleccionado && asignacion.anio === anioSeleccionado && asignacion.dni === dniSeleccionado;
        });

        // Si el DNI está repetido para el mes y año seleccionados, mostrar un mensaje de error
        if (dniRepetido) {
            Swal.fire({
                icon: 'error',
                title: 'El DNI ya ha sido asignado para el mes y año seleccionados.',
                confirmButtonText: 'Aceptar'
            });
            return false; // Evitar el envío del formulario
        } else {
            // Si el DNI no está repetido, se procede a enviar el formulario
            document.querySelector("form").submit();
        }
    } else {
        // Si no se han seleccionado el mes, el año y/o el DNI del sereno, mostrar un mensaje de error
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Por favor, selecciona el mes, el año y el sereno antes de continuar.',
            confirmButtonText: 'Aceptar'
        });
        return false; // Evitar el envío del formulario
    }
}