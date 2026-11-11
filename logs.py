# ============================================
# SISTEMA SOFTWARE FJ
# Archivo: logs.py
# Descripcion: Registro de errores y eventos
# ============================================

import logging
import os


def configurar_logs():
    """
    Configura el sistema de registro de eventos
    y errores de la aplicacion Software FJ.
    """

    # Nombre del archivo donde se guardaran los registros.
    archivo_logs = "software_fj.log"

    # Crear el registrador principal.
    logger = logging.getLogger("SoftwareFJ")

    # Establecer el nivel de registro.
    logger.setLevel(logging.INFO)

    # Evitar duplicar los registros.
    if logger.handlers:
        return logger

    # Formato de los mensajes registrados.
    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Crear el archivo de registro.
    manejador_archivo = logging.FileHandler(
        archivo_logs,
        encoding="utf-8"
    )

    manejador_archivo.setLevel(logging.INFO)
    manejador_archivo.setFormatter(formato)

    # Mostrar tambien los registros en la consola.
    manejador_consola = logging.StreamHandler()

    manejador_consola.setLevel(logging.WARNING)
    manejador_consola.setFormatter(formato)

    # Agregar los manejadores al registrador.
    logger.addHandler(manejador_archivo)
    logger.addHandler(manejador_consola)

    logger.info("Sistema Software FJ iniciado correctamente.")

    return logger