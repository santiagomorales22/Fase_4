# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: excepciones.py
# Descripción: Excepciones personalizadas
# ============================================

class ErrorSistema(Exception):
    """Excepción base para los errores del sistema."""
    pass


class ErrorValidacion(ErrorSistema):
    """Error cuando los datos ingresados no son válidos."""
    pass


class ErrorCliente(ErrorSistema):
    """Error relacionado con el registro de clientes."""
    pass


class ErrorServicio(ErrorSistema):
    """Error relacionado con los servicios."""
    pass


class ErrorReserva(ErrorSistema):
    """Error relacionado con las reservas."""
    pass


class ServicioNoDisponible(ErrorServicio):
    """Error cuando un servicio no está disponible."""
    pass


class OperacionNoPermitida(ErrorSistema):
    """Error cuando se intenta realizar una operación no permitida."""
    pass


class ErrorCalculo(ErrorSistema):
    """Error cuando ocurre un problema al calcular los costos."""
    pass