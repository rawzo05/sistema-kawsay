from datetime import datetime

from paciente import Paciente
from medico import Medico
from cita import Cita


pacientes: list = []
medicos: list = []
citas: list = []


# --- Validaciones (paradigma estructurado) ---

def _normalizar_codigo(codigo: str) -> str:
    return str(codigo).strip().upper()


def _validar_edad(edad_texto: str, errores: list):
    try:
        edad = int(edad_texto)
    except ValueError:
        errores.append("La edad debe ser un número entero.")
        return None
    if edad < 0 or edad > 120:
        errores.append("La edad debe estar entre 0 y 120 años.")
    return edad


def _validar_fecha(fecha_texto: str, errores: list) -> None:
    try:
        datetime.strptime(fecha_texto.strip(), "%Y-%m-%d")
    except ValueError:
        errores.append("La fecha debe tener el formato AAAA-MM-DD (ej. 2026-04-15).")


def buscar_por_codigo(codigo: str, coleccion: list):
    codigo = _normalizar_codigo(codigo)
    for elemento in coleccion:
        if elemento.codigo == codigo:
            return elemento
    return None


def _codigo_persona_existe(codigo: str) -> bool:
    return (buscar_por_codigo(codigo, pacientes) is not None
            or buscar_por_codigo(codigo, medicos) is not None)


def _lanzar_si_hay_errores(errores: list) -> None:
    if errores:
        raise ValueError(" | ".join(errores))


# --- Patrón de diseño: Factory ---

def crear_persona(tipo: str, codigo: str, nombre: str, dato_extra):
    if tipo == "paciente":
        return Paciente(codigo, nombre, dato_extra)
    if tipo == "medico":
        return Medico(codigo, nombre, dato_extra)
    raise ValueError(f"Tipo de persona no reconocido: {tipo}")


# --- RF01: registrar paciente ---

def registrar_paciente(codigo: str, nombre: str, edad_texto: str) -> Paciente:
    errores = []
    codigo = _normalizar_codigo(codigo)
    if not codigo:
        errores.append("El código no puede estar vacío.")
    if not nombre.strip():
        errores.append("El nombre no puede estar vacío.")
    if codigo and _codigo_persona_existe(codigo):
        errores.append("El paciente ya existe.")
    edad = _validar_edad(edad_texto, errores)
    _lanzar_si_hay_errores(errores)

    paciente = crear_persona("paciente", codigo, nombre, edad)
    pacientes.append(paciente)
    return paciente


# --- RF02: registrar médico ---

def registrar_medico(codigo: str, nombre: str, especialidad: str) -> Medico:
    errores = []
    codigo = _normalizar_codigo(codigo)
    if not codigo:
        errores.append("El código no puede estar vacío.")
    if not nombre.strip():
        errores.append("El nombre no puede estar vacío.")
    if codigo and _codigo_persona_existe(codigo):
        errores.append("El médico ya existe.")
    if especialidad not in Medico.ESPECIALIDADES_VALIDAS:
        opciones = ", ".join(Medico.ESPECIALIDADES_VALIDAS)
        errores.append(f"Especialidad no válida. Opciones: {opciones}")
    _lanzar_si_hay_errores(errores)

    medico = crear_persona("medico", codigo, nombre, especialidad)
    medicos.append(medico)
    return medico


# --- RF04: programar cita ---

def programar_cita(codigo_cita: str, codigo_paciente: str,
                    codigo_medico: str, fecha: str) -> Cita:
    errores = []
    codigo_cita = _normalizar_codigo(codigo_cita)
    if not codigo_cita:
        errores.append("El código de la cita no puede estar vacío.")
    elif buscar_por_codigo(codigo_cita, citas) is not None:
        errores.append("La cita ya existe.")
    if not fecha.strip():
        errores.append("La fecha no puede estar vacía.")
    else:
        _validar_fecha(fecha, errores)

    paciente = buscar_por_codigo(codigo_paciente, pacientes)
    if paciente is None:
        errores.append(f"Referencia inválida: el paciente {codigo_paciente} no existe.")
    medico = buscar_por_codigo(codigo_medico, medicos)
    if medico is None:
        errores.append(f"Referencia inválida: el médico {codigo_medico} no existe.")
    _lanzar_si_hay_errores(errores)

    cita = Cita(codigo_cita, paciente, medico, fecha)
    citas.append(cita)
    return cita


# --- RF05: registrar atención ---

def registrar_atencion(codigo_cita: str, diagnostico: str, observaciones: str) -> Cita:
    errores = []
    cita = buscar_por_codigo(codigo_cita, citas)
    if cita is None:
        errores.append(f"Referencia inválida: la cita {codigo_cita} no existe.")
    if not diagnostico.strip():
        errores.append("El diagnóstico no puede estar vacío.")
    _lanzar_si_hay_errores(errores)

    cita.registrar_atencion(diagnostico, observaciones)
    return cita


# --- Paradigma funcional: consultas declarativas ---

def buscar_por_especialidad(especialidad: str) -> list:
    return list(filter(lambda medico: medico.especialidad == especialidad, medicos))


def consultar_historial(codigo_paciente: str) -> list:
    codigo_paciente = _normalizar_codigo(codigo_paciente)
    return list(filter(
        lambda cita: cita.paciente.codigo == codigo_paciente and cita.atendida,
        citas
    ))
