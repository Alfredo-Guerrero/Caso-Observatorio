from datetime import datetime

def formatear_fecha(fecha_str):
    """Formatea una fecha de string al formato DD/MM/AAAA."""
    fecha_date = datetime.strptime(fecha_str, '%Y-%m-%d')
    return fecha_date.strftime('%d/%m/%Y')


