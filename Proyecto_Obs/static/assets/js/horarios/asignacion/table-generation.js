// Función para generar la tabla de asignaciones por sereno
function generarTablaAsignacionesPorSereno() {
    var tabla = '<table id="dataTable2" class="table table-sm table-striped table-hover table-bordered shadow-lg dt-responsive nowrap" style="width:100%">';
    tabla += '<thead><tr><th class="sticky-sereno"><input type="checkbox" id="seleccionarTodos"></th><th class="sticky-sereno">Sereno</th>';

    // Encabezados de las fechas
    for (var sereno in asignacionesPorSereno) {
        if (asignacionesPorSereno.hasOwnProperty(sereno)) {
            var asignaciones = asignacionesPorSereno[sereno];
            asignaciones.forEach(function(asignacion) {
                // Formatear la fecha para mostrarla verticalmente
                var fecha = '<div>' + asignacion.fecha + '</div>';
                tabla += '<th>' + fecha + '</th>';
            });
            break; // Solo necesitamos las fechas de la primera fila
        }
    }



    tabla += '</tr></thead><tbody>';

    // Iterar sobre las asignaciones
    for (var sereno in asignacionesPorSereno) {
        if (asignacionesPorSereno.hasOwnProperty(sereno)) {
            tabla += '<tr><td class="sticky-sereno"><input type="checkbox" class="check-sereno" data-sereno="' + sereno + '" data-dni="' + asignacionesPorSereno[sereno][0].detalles.dni + '" data-mes="' + asignacionesPorSereno[sereno][0].detalles.mes_asig + '"></td><td class="sticky-sereno">' + sereno + '</td>'; // Establecer un ancho máximo para la celda del nombre del sereno

            // Iterar sobre las asignaciones del sereno actual
            asignacionesPorSereno[sereno].forEach(function(asignacion) {
                // Asignar badge según el turno
                var badgeClass = '';
                switch (asignacion.turno) {
                    case 'M':
                        badgeClass = 'badge-primary';
                        break;
                    case 'T':
                        badgeClass = 'badge-warning';
                        break;
                    case 'N':
                        badgeClass = 'badge-dark';
                        break;
                    case 'D':
                        badgeClass = 'badge-success';
                        break;
                    case 'V':
                        badgeClass = 'badge-info';
                        break;
                    case 'F':
                        badgeClass = 'badge-danger';
                        break;
                    case 'L':
                        badgeClass = 'badge-secondary';
                        break;
                    default:
                        badgeClass = 'badge-secondary';
                }

                // Agregar ID único a la celda
                var celdaId = sereno.replace(/\s+/g, '') + '-' + asignacion.fecha.replace(/\s+/g, '');

                // Construir la celda de la tabla
                tabla += '<td id="' + celdaId + '" class="ver-datos-relacionados';

                // Verificar si hay información de asistencia
                if (asignacion.detalles.ASIS_chTIPREG) {
                    // Si hay información de asistencia, agregar una clase adicional
                    tabla += ' con-asistencia';
                }

                tabla += '" data-asignacion-id="' + asignacion.id + '" data-detalles=\'' + JSON.stringify(asignacion.detalles) + '\' onclick="mostrarDetallesEnModal(this)">';

                // Validar si solo hay un badge (el del turno)
                if (!asignacion.detalles.ASIS_chTIPREG) {
                    tabla += '<span class="badge ' + badgeClass + ' d-flex justify-content-center align-items-center w-100">' + asignacion.turno + '</span>';
                } else {
                    // Si hay información de asistencia, se muestra tanto el badge de turno como el de asistencia
                    tabla += '<div class="d-flex">';
                    tabla += '<span class="badge ' + badgeClass + ' d-inline-block mr-1">' + asignacion.turno + '</span>';
                    tabla += obtenerTextoAsistencia(asignacion.detalles.ASIS_chTIPREG);
                    tabla += '</div>';
                }

                tabla += '<input type="hidden" class="asignacion-id" value="' + asignacion.id + '">';
                tabla += '</td>';

            });

            tabla += '</tr>';
        }
    }

    // Función para obtener el texto de la asistencia
    function obtenerTextoAsistencia(asistencia) {
        var textoAsistencia = '';
        switch (asistencia) {
            case 'De':
                textoAsistencia = '<span class="badge badge-success ml-2">D</span>';
                break;
            case 'Asis':
                textoAsistencia = '<span class="badge badge-success ml-2">A</span>';
                break;
            case 'Inasis':
                textoAsistencia = '<span class="badge badge-danger ml-2">F</span>';
                break;
            case 'Onom':
                textoAsistencia = '<span>&#x1F382;</span>';
                break;
            case 'PermP':
                textoAsistencia = '<span class="badge badge-secondary ml-2">L</span>';
                break;
            case 'PermS':
                textoAsistencia = '<span class="badge badge-purple ml-2">PS</span>';
                break;
            case 'Vac':
                textoAsistencia = '<span class="badge badge-info ml-2">V</span>';
                break;
            default:
                textoAsistencia = ''; // Si es desconocido, dejar vacío
        }
        return textoAsistencia;
    }


    tabla += '</tbody></table>';

    // Insertar la tabla en el div correspondiente
    document.getElementById('dtabla-asignaciones').innerHTML = tabla;

    // Agregar funcionalidad al checkbox de seleccionar todos
    document.getElementById('seleccionarTodos').addEventListener('change', function() {
        var checkboxes = document.querySelectorAll('.check-sereno, .check-eliminar'); // Incluye los checkboxes de las filas y de la eliminación masiva
        var isChecked = this.checked; // Almacenar el estado del checkbox de la cabecera
        checkboxes.forEach(function(checkbox) {
            checkbox.checked = isChecked; // Usar el estado almacenado para marcar o desmarcar cada checkbox
        });
    });

}


// Función para mostrar los detalles de la asignación en un modal
function mostrarDetallesEnModal(celda) {
    var detalles = JSON.parse(celda.getAttribute('data-detalles'));

    // Asignar los valores de los detalles a los inputs del modal
    document.getElementById('codigo').value = detalles.codigo;
    document.getElementById('doc').value = detalles.dni;
    document.getElementById('colaborador').value = detalles.sereno;
    document.getElementById('fecha').value = detalles.dia;
    document.getElementById('horario').value = detalles.horario;
    document.getElementById('perf').value = detalles.perfil;
    document.getElementById('patron').value = detalles.patron;
    document.getElementById('grup').value = detalles.grupo;
    document.getElementById('juridiccion').value = detalles.juridiccion;

    // Obtener el elemento donde se mostrará el texto del turno y asitencia
    var elementoTurno = document.getElementById('turno');
    var elementoAsistencia = document.getElementById('asistencia');
    var elementoMarcacion = document.getElementById('marcacionTexto');
    var elementoTardanza = document.getElementById('tardanza');

    // Mostrar el texto del turno, asistencia y asignar la clase de Bootstrap
    elementoTardanza.textContent = detalles.tardanza;
    elementoMarcacion.textContent = detalles.marcacion;
    asignarTextoYClase(elementoTurno, detalles.turno);
    asistenciaTextoYClase(elementoAsistencia, detalles.ASIS_chTIPREG);



    // Mostrar el modal
    $('#miModal').modal('show');
}

// Llamar a la función para generar la tabla de asignaciones por sereno
generarTablaAsignacionesPorSereno();