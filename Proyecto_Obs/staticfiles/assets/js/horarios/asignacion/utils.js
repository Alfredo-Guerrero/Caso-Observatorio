function asignarTextoYClase(elemento, turno) {
    var textoTurno = '';
    var badgeClass = '';
    switch (turno) {
        case 'M':
            textoTurno = 'Mañana';
            badgeClass = 'badge-primary';
            break;
        case 'T':
            textoTurno = 'Tarde';
            badgeClass = 'badge-warning';
            break;
        case 'N':
            textoTurno = 'Noche';
            badgeClass = 'badge-dark';
            break;
        case 'D':
            textoTurno = 'Descanso';
            badgeClass = 'badge-success';
            break;
        case 'V':
            textoTurno = 'Vacaciones';
            badgeClass = 'badge-info';
            break;
        case 'F':
            textoTurno = 'Falta';
            badgeClass = 'badge-danger';
            break;
        case 'L':
            textoTurno = 'Licencia';
            badgeClass = 'badge-secondary';
            break;
        default:
            textoTurno = 'Desconocido';
            badgeClass = 'badge-secondary';
    }
    // Asignar el texto del turno y la clase de Bootstrap al elemento
    elemento.textContent = textoTurno;
    elemento.classList.remove('badge-primary', 'badge-warning', 'badge-dark', 'badge-success', 'badge-info', 'badge-danger', 'badge-secondary');
    elemento.classList.add('badge', badgeClass);
}


function asistenciaTextoYClase(elemento, asistencia) {
    var textoAsistencia = '';
    var colorClase = '';
    var icono = '';
    switch (asistencia) {
        case 'Asis':
            textoAsistencia = '<strong>Asistencia</strong>';
            colorClase = 'text-success';
            break;
        case 'Inasis':
            textoAsistencia = '<strong>Falta</strong>';
            colorClase = 'text-danger';
            break;
        case 'Onom':
            textoAsistencia = '<strong>Cumpleaños</strong> ' + '&#x1F382;';
            colorClase = 'text-dark';
            break;
        case 'PermP':
            textoAsistencia = '<strong>Permiso Personal</strong>';
            colorClase = 'text-secondary';
            break;
        case 'PermS':
            textoAsistencia = '<strong>Permiso por Salud</strong>';
            colorClase = 'text-purple'; // Puedes cambiar el color morado según tu preferencia
            break;
        case 'Vac':
            textoAsistencia = '<strong>Vacaciones</strong>';
            colorClase = 'text-info';
            break;
        default:
            textoAsistencia = '<strong>Desconocido</strong>';
            colorClase = 'text-secondary';
    }
    // Asignar el texto de la asistencia y el icono (si lo hay) con el color al elemento
    elemento.innerHTML = textoAsistencia + ' ' + icono;
    elemento.classList.remove('text-success', 'text-danger', 'text-dark', 'text-secondary', 'text-purple', 'text-info');
    elemento.classList.add(colorClase);
}