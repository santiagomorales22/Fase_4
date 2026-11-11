# ============================================================
# SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ
# Fase 4 - Programacion
# ============================================================

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from excepciones import ErrorSistema, OperacionNoPermitida
from logs import configurar_logs


# Configuracion del registro de eventos
logger = configurar_logs()

# Listas internas del sistema
clientes = []
servicios = []
reservas = []


# ============================================================
# FUNCIONES GENERALES
# ============================================================

def mostrar_titulo():
    print("\n" + "=" * 65)
    print(" SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print(" Clientes, servicios y reservas")
    print("=" * 65)


def registrar_cliente(cliente):
    clientes.append(cliente)
    logger.info("Cliente registrado: %s", cliente.obtener_identificacion())


def registrar_servicio(servicio):
    servicios.append(servicio)
    logger.info("Servicio registrado: %s", servicio.obtener_identificacion())


def registrar_reserva(reserva):
    reservas.append(reserva)
    logger.info("Reserva registrada: %s", reserva.obtener_identificacion())


def mostrar_clientes():
    print("\n========== LISTADO DE CLIENTES ==========")

    for cliente in clientes:
        print(cliente.obtener_resumen())


def mostrar_servicios():
    print("\n========== LISTADO DE SERVICIOS ==========")

    for servicio in servicios:
        print(servicio.obtener_resumen())


def mostrar_reservas():
    print("\n========== LISTADO DE RESERVAS ==========")

    for reserva in reservas:
        print(reserva.obtener_resumen())


# ============================================================
# PRUEBAS DEL SISTEMA
# ============================================================

def ejecutar_pruebas():

    mostrar_titulo()

    # OPERACION 1: Registro de cliente valido

    print("\nOPERACION 1: Registro de cliente valido")

    try:
        cliente1 = Cliente(
            "1001",
            "Carlos Morales",
            "carlos@gmail.com",
            "3123456789"
        )

        registrar_cliente(cliente1)
        print("Cliente registrado correctamente.")
        print(cliente1.obtener_resumen())

    except ErrorSistema as error:
        print("Error:", error)
        logger.error("Error al registrar cliente: %s", error)
        return

    # OPERACION 2: Registro de cliente invalido

    print("\nOPERACION 2: Registro de cliente con correo incorrecto")

    try:
        cliente_invalido = Cliente(
            "1002",
            "Juan Perez",
            "correo_incorrecto",
            "3101234567"
        )

        registrar_cliente(cliente_invalido)

    except ErrorSistema as error:
        print("Error controlado:", error)
        logger.warning("Se intento registrar un cliente invalido.")

    # OPERACION 3: Servicio de reserva de sala

    print("\nOPERACION 3: Creacion de servicio de reserva de sala")

    try:
        servicio1 = ReservaSala(
            "S001",
            "Sala de reuniones",
            50000,
            10
        )

        registrar_servicio(servicio1)
        print("Servicio de sala creado correctamente.")
        print(servicio1.obtener_resumen())

    except ErrorSistema as error:
        print("Error:", error)
        return

    # OPERACION 4: Servicio de alquiler de equipo

    print("\nOPERACION 4: Creacion de servicio de alquiler de equipo")

    try:
        servicio2 = AlquilerEquipo(
            "S002",
            "Alquiler de computadores",
            30000,
            2
        )

        registrar_servicio(servicio2)
        print("Servicio de alquiler creado correctamente.")
        print(servicio2.obtener_resumen())

    except ErrorSistema as error:
        print("Error:", error)

    # OPERACION 5: Servicio de asesoria especializada

    print("\nOPERACION 5: Creacion de servicio de asesoria")

    try:
        servicio3 = AsesoriaEspecializada(
            "S003",
            "Asesoria tecnologica",
            80000,
            "Ingenieria de sistemas"
        )

        registrar_servicio(servicio3)
        print("Servicio de asesoria creado correctamente.")
        print(servicio3.obtener_resumen())

    except ErrorSistema as error:
        print("Error:", error)

    # OPERACION 6: Servicio con tarifa incorrecta

    print("\nOPERACION 6: Servicio con tarifa incorrecta")

    try:
        servicio_invalido = ReservaSala(
            "S004",
            "Sala de prueba",
            -5000,
            5
        )

        registrar_servicio(servicio_invalido)

    except ErrorSistema as error:
        print("Error controlado:", error)
        logger.warning("Se intento crear un servicio con tarifa invalida.")

    # OPERACION 7: Calculo del costo

    print("\nOPERACION 7: Calculo del costo del servicio")

    try:
        costo = servicio1.calcular_costo(
            2,
            descuento=10,
            impuesto=19
        )

        print("Calculo realizado correctamente.")
        print(f"Costo del servicio: ${costo:,.2f}")

    except ErrorSistema as error:
        print("Error:", error)

    # OPERACION 8: Creacion de reserva

    print("\nOPERACION 8: Creacion de reserva")

    try:
        reserva1 = Reserva(
            "R001",
            cliente1,
            servicio1,
            2
        )

        registrar_reserva(reserva1)
        print("Reserva creada correctamente.")
        print(reserva1.obtener_resumen())

    except ErrorSistema as error:
        print("Error:", error)
        return

    # OPERACION 9: Confirmacion de reserva

    print("\nOPERACION 9: Confirmacion de reserva")

    try:
        reserva1.confirmar()
        print("Reserva confirmada correctamente.")

    except ErrorSistema as error:
        print("Error:", error)

    # OPERACION 10: Procesamiento de reserva

    print("\nOPERACION 10: Procesamiento de reserva")

    try:
        costo_reserva = reserva1.procesar(
            descuento=10,
            impuesto=19
        )

        print("Reserva procesada correctamente.")
        print(f"Costo final: ${costo_reserva:,.2f}")

    except ErrorSistema as error:
        print("Error:", error)

    # OPERACION 11: Intento de cancelar reserva procesada

    print("\nOPERACION 11: Cancelacion no permitida")

    try:
        reserva1.cancelar()

    except OperacionNoPermitida as error:
        print("Error controlado:", error)
        logger.warning("Se intento cancelar una reserva procesada.")

    except ErrorSistema as error:
        print("Error:", error)

    # OPERACION 12: Reserva con duracion invalida

    print("\nOPERACION 12: Reserva con duracion incorrecta")

    try:
        reserva_invalida = Reserva(
            "R003",
            cliente1,
            servicio1,
            -5
        )

        registrar_reserva(reserva_invalida)

    except ErrorSistema as error:
        print("Error controlado:", error)
        logger.warning("No se pudo crear la reserva: %s", error)

    # RESUMEN FINAL

    print("\n" + "=" * 65)
    print("RESUMEN FINAL DEL SISTEMA")
    print("=" * 65)

    mostrar_clientes()
    mostrar_servicios()
    mostrar_reservas()

    print("\nPruebas finalizadas.")
    logger.info("Finalizacion de las pruebas del sistema.")


# ============================================================
# EJECUCION PRINCIPAL
# ============================================================

if __name__ == "__main__":

    try:
        ejecutar_pruebas()

    except Exception as error:
        logger.exception("Error general: %s", error)

    finally:
        print("\nFin del programa Software FJ.")