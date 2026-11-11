# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: servicios.py
# Descripcion: Gestion de servicios
# ============================================

from abc import ABC, abstractmethod

from entidades import Entidad
from excepciones import ErrorServicio, ErrorValidacion


class Servicio(Entidad, ABC):
    """
    Clase abstracta que representa los servicios
    ofrecidos por la empresa Software FJ.
    """

    def __init__(self, identificacion, nombre, tarifa):
        super().__init__(identificacion)

        self._nombre = nombre
        self._tarifa = tarifa

        self.validar()

    def validar(self):
        """Valida la informacion general del servicio."""

        if not isinstance(self._identificacion, str) or not self._identificacion.strip():
            raise ErrorServicio("La identificacion es obligatoria.")

        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ErrorValidacion("El nombre del servicio es obligatorio.")

        if isinstance(self._tarifa, bool) or not isinstance(self._tarifa, (int, float)):
            raise ErrorValidacion("La tarifa debe ser numerica.")

        if self._tarifa <= 0:
            raise ErrorValidacion("La tarifa debe ser mayor que cero.")

        return True

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        """Calcula el costo del servicio."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Describe las caracteristicas del servicio."""
        pass

    def obtener_resumen(self):
        """Muestra informacion general del servicio."""

        return (
            f"Identificacion: {self._identificacion}\n"
            f"Nombre: {self._nombre}\n"
            f"Tarifa: ${self._tarifa:,.2f}\n"
            f"Estado: {'Activo' if self._activo else 'Inactivo'}"
        )


class ReservaSala(Servicio):
    """Servicio de reserva de salas."""

    def __init__(self, identificacion, nombre, tarifa, capacidad):
        self.__capacidad = capacidad

        super().__init__(identificacion, nombre, tarifa)

    def validar(self):

        super().validar()

        if isinstance(self.__capacidad, bool) or not isinstance(self.__capacidad, int):
            raise ErrorValidacion("La capacidad debe ser un numero entero.")

        if self.__capacidad <= 0:
            raise ErrorValidacion("La capacidad debe ser mayor que cero.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        self._validar_calculo(duracion, descuento, impuesto)

        subtotal = self._tarifa * duracion
        total = subtotal - (subtotal * descuento / 100)
        total += total * impuesto / 100

        return round(total, 2)

    def describir_servicio(self):

        return (
            f"Reserva de sala: {self._nombre}. "
            f"Capacidad: {self.__capacidad} personas."
        )

    def obtener_capacidad(self):
        return self.__capacidad

    def _validar_calculo(self, duracion, descuento, impuesto):

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ErrorValidacion("La duracion debe ser mayor que cero.")

        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 100:
            raise ErrorValidacion("El descuento debe estar entre 0 y 100.")

        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 100:
            raise ErrorValidacion("El impuesto debe estar entre 0 y 100.")


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos tecnologicos."""

    def __init__(self, identificacion, nombre, tarifa, cantidad):
        self.__cantidad = cantidad

        super().__init__(identificacion, nombre, tarifa)

    def validar(self):

        super().validar()

        if isinstance(self.__cantidad, bool) or not isinstance(self.__cantidad, int):
            raise ErrorValidacion("La cantidad debe ser un numero entero.")

        if self.__cantidad <= 0:
            raise ErrorValidacion("La cantidad debe ser mayor que cero.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        ReservaSala._validar_calculo(self, duracion, descuento, impuesto)

        subtotal = self._tarifa * duracion * self.__cantidad
        total = subtotal - (subtotal * descuento / 100)
        total += total * impuesto / 100

        return round(total, 2)

    def describir_servicio(self):

        return (
            f"Alquiler de equipos: {self._nombre}. "
            f"Cantidad disponible: {self.__cantidad}."
        )

    def obtener_cantidad(self):
        return self.__cantidad


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoria especializada."""

    def __init__(self, identificacion, nombre, tarifa, especialidad):
        self.__especialidad = especialidad

        super().__init__(identificacion, nombre, tarifa)

    def validar(self):

        super().validar()

        if not isinstance(self.__especialidad, str) or not self.__especialidad.strip():
            raise ErrorValidacion("La especialidad es obligatoria.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):

        ReservaSala._validar_calculo(self, duracion, descuento, impuesto)

        subtotal = self._tarifa * duracion
        total = subtotal - (subtotal * descuento / 100)
        total += total * impuesto / 100

        return round(total, 2)

    def describir_servicio(self):

        return (
            f"Asesoria especializada: {self._nombre}. "
            f"Especialidad: {self.__especialidad}."
        )

    def obtener_especialidad(self):
        return self.__especialidad