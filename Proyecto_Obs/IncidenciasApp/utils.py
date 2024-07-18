from datetime import datetime

def formatear_fecha(fecha_str):
    """Formatea una fecha de string al formato DD/MM/AAAA."""
    fecha_date = datetime.strptime(fecha_str, '%Y-%m-%d')
    return fecha_date.strftime('%d/%m/%Y')

def formatear_hora(hora_str):
    """Formatea una hora de string al formato HH:MM:SS."""
    try:
        hora_time = datetime.strptime(hora_str, '%H:%M:%S')
    except ValueError:
        # Si no se pueden analizar los segundos, intenta formatear sin segundos
        hora_time = datetime.strptime(hora_str, '%H:%M')
    return hora_time.strftime('%H:%M:%S')