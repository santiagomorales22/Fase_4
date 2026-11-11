# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: clientes.py
# Descripción: Registro y gestión de clientes
# ============================================

import re

from entidades import Entidad
from excepciones import ErrorCliente, ErrorValidacion


class Cliente(Entidad):
    """
    Clase que representa un cliente de Software FJ.
    Hereda de la clase abstracta Entidad.
    """

    def __init__(self, identificacion, nombre, correo, telefono):

        super().__init__(identificacion)

        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar()

    def validar(self):
        """Valida los datos personales del cliente."""

        if not isinstance(self._identificacion, str) or not self._identificacion.strip():
            raise ErrorCliente("La identificación es obligatoria.")

        if not isinstance(self.__nombre, str) or len(self.__nombre.strip()) < 3:
            raise ErrorValidacion("El nombre debe tener al menos 3 caracteres.")

        if not isinstance(self.__correo, str):
            raise ErrorValidacion("El correo debe ser un texto válido.")

        if not re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", self.__correo):
            raise ErrorValidacion("El correo electrónico no es válido.")

        if not isinstance(self.__telefono, str) or not self.__telefono.isdigit():
            raise ErrorValidacion("El teléfono debe contener únicamente números.")

        if not 7 <= len(self.__telefono) <= 15:
            raise ErrorValidacion("El teléfono debe tener entre 7 y 15 dígitos.")

        return True

    def obtener_resumen(self):
        """Devuelve un resumen de la información del cliente."""

        return (
            f"Identificación: {self._identificacion}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}\n"
            f"Estado: {'Activo' if self._activo else 'Inactivo'}"
        )

    def obtener_nombre(self):
        """Devuelve el nombre del cliente."""
        return self.__nombre

    def obtener_correo(self):
        """Devuelve el correo electrónico."""
        return self.__correo

    def obtener_telefono(self):
        """Devuelve el teléfono del cliente."""
        return self.__telefono

    def actualizar_correo(self, nuevo_correo):
        """Permite actualizar el correo del cliente."""

        correo_anterior = self.__correo
        self.__correo = nuevo_correo

        try:
            self.validar()
        except ErrorValidacion:
            self.__correo = correo_anterior
            raise