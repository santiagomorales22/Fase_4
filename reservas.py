# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: reservas.py
# Descripcion: Gestion de reservas
# ============================================

import logging

from entidades import Entidad
from clientes import Cliente
from servicios import Servicio

from excepciones import (
    ErrorReserva,
    ErrorValidacion,
    ErrorCalculo,
    OperacionNoPermitida,
    ServicioNoDisponible
)


logger = logging.getLogger("SoftwareFJ")


class Reserva(Entidad):
    """
    Clase encargada de administrar las reservas
    realizadas por los clientes de Software FJ.
    """

    def __init__(self, identificacion, cliente, servicio, duracion):

        super().__init__(identificacion)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = 0

        self.validar()

        logger.info(
            "Reserva %s creada correctamente.",
            identificacion
        )

    def validar(self):
        """Valida la informacion de la reserva."""

        if not isinstance(self._identificacion, str) or not self._identificacion.strip():
            raise ErrorReserva("La identificacion de la reserva es obligatoria.")

        if not isinstance(self.__cliente, Cliente):
            raise ErrorValidacion("Debe seleccionar un cliente valido.")

        if not isinstance(self.__servicio, Servicio):
            raise ErrorValidacion("Debe seleccionar un servicio valido.")

        if not self.__cliente.esta_activo():
            raise ErrorReserva("El cliente se encuentra inactivo.")

        if not self.__servicio.esta_activo():
            raise ServicioNoDisponible("El servicio no esta disponible.")

        if (
            isinstance(self.__duracion, bool)
            or not isinstance(self.__duracion, (int, float))
            or self.__duracion <= 0
        ):
            raise ErrorValidacion("La duracion debe ser mayor que cero.")

        return True

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.__estado != "Pendiente":
            raise OperacionNoPermitida(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"

        logger.info(
            "Reserva %s confirmada.",
            self._identificacion
        )

        return True

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""

        if self.__estado not in ("Pendiente", "Confirmada"):
            raise OperacionNoPermitida(
                "La reserva no puede cancelarse."
            )

        self.__estado = "Cancelada"

        logger.info(
            "Reserva %s cancelada.",
            self._identificacion
        )

        return True

    def procesar(self, descuento=0, impuesto=0):
        """
        Procesa una reserva confirmada y calcula su costo.
        """

        try:

            if self.__estado != "Confirmada":
                raise OperacionNoPermitida(
                    "La reserva debe estar confirmada para procesarse."
                )

            self.validar()

            self.__costo = self.__servicio.calcular_costo(
                self.__duracion,
                descuento,
                impuesto
            )

        except OperacionNoPermitida:
            logger.warning(
                "Operacion no permitida en reserva %s.",
                self._identificacion
            )
            raise

        except Exception as error:

            logger.exception(
                "Error al procesar la reserva %s.",
                self._identificacion
            )

            raise ErrorCalculo(
                "No fue posible calcular el costo de la reserva."
            ) from error

        else:

            self.__estado = "Procesada"

            logger.info(
                "Reserva %s procesada. Costo: %.2f",
                self._identificacion,
                self.__costo
            )

            return self.__costo

        finally:

            logger.info(
                "Finalizo el intento de procesamiento de la reserva %s.",
                self._identificacion
            )

    def obtener_estado(self):
        """Devuelve el estado actual de la reserva."""
        return self.__estado

    def obtener_costo(self):
        """Devuelve el costo de la reserva."""
        return self.__costo

    def obtener_cliente(self):
        """Devuelve el cliente asociado."""
        return self.__cliente

    def obtener_servicio(self):
        """Devuelve el servicio asociado."""
        return self.__servicio

    def obtener_resumen(self):
        """Genera un resumen de la reserva."""

        return (
            f"Reserva: {self._identificacion}\n"
            f"Cliente: {self.__cliente.obtener_nombre()}\n"
            f"Servicio: {self.__servicio._nombre}\n"
            f"Duracion: {self.__duracion} horas\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.__costo:,.2f}"
        )