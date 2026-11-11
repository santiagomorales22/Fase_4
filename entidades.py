# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: entidades.py
# Descripción: Clase abstracta general
# ============================================

from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad
    general dentro del sistema Software FJ.
    """

    def __init__(self, identificacion):
        self._identificacion = identificacion
        self._activo = True

    @abstractmethod
    def validar(self):
        """
        Método abstracto para validar la información
        de cada entidad.
        """
        pass

    @abstractmethod
    def obtener_resumen(self):
        """
        Método abstracto para obtener información
        general de cada entidad.
        """
        pass

    def activar(self):
        """Activa una entidad."""
        self._activo = True

    def desactivar(self):
        """Desactiva una entidad."""
        self._activo = False

    def esta_activo(self):
        """Consulta el estado de una entidad."""
        return self._activo

    def obtener_identificacion(self):
        """Devuelve la identificación de la entidad."""
        return self._identificacion