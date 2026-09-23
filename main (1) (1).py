import gestion


def mostrar_menu() -> None:
    print("\n===== SISTEMA KAWSAY =====")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Buscar por código")
    print("4. Programar cita")
    print("5. Registrar atención")
    print("6. Buscar médicos por especialidad")
    print("7. Consultar historial de un paciente")
    print("0. Salir")


def preguntar_continuar(accion: str) -> bool:
    while True:
        respuesta = input(f"\n¿Desea {accion} de nuevo? (S/N): ").strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("Respuesta no válida. Ingrese S para continuar o N para volver al menú.")


def registrar_paciente_menu() -> None:
    while True:
        codigo = input("Código nuevo para el paciente (ej. P005): ").strip()
        nombre = input("Nombre del paciente: ").strip()
        edad_texto = input("Edad: ").strip()
        try:
            paciente = gestion.registrar_paciente(codigo, nombre, edad_texto)
            print(f"Registro exitoso: {paciente}")
        except ValueError as error:
            print(f"Error: {error}")
        if not preguntar_continuar("registrar un paciente"):
            break


def elegir_de_lista(lista: list, mensaje_vacio: str):
    if not lista:
        print(mensaje_vacio)
        return None
    for i, elemento in enumerate(lista, start=1):
        print(f"  {i}. {elemento}")
    while True:
        opcion = input("Seleccione un número (Enter para cancelar): ").strip()
        if opcion == "":
            return None
        if opcion.isdigit() and 1 <= int(opcion) <= len(lista):
            return lista[int(opcion) - 1]
        print("Opción no válida. Ingrese un número de la lista.")


def elegir_especialidad() -> str:
    especialidades = gestion.Medico.ESPECIALIDADES_VALIDAS
    while True:
        print("Especialidades disponibles:")
        for i, especialidad in enumerate(especialidades, start=1):
            print(f"  {i}. {especialidad}")
        opcion = input("Seleccione el número de la especialidad: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(especialidades):
            return especialidades[int(opcion) - 1]
        print("Opción no válida. Ingrese un número de la lista.")


def registrar_medico_menu() -> None:
    while True:
        codigo = input("Código nuevo para el médico (ej. M011): ").strip()
        nombre = input("Nombre del médico: ").strip()
        especialidad = elegir_especialidad()
        try:
            medico = gestion.registrar_medico(codigo, nombre, especialidad)
            print(f"Registro exitoso: {medico}")
        except ValueError as error:
            print(f"Error: {error}")
        if not preguntar_continuar("registrar un médico"):
            break


def buscar_por_codigo_menu() -> None:
    while True:
        codigo = input("Código a buscar (ej. P001, M001 o C001): ").strip()
        resultado = (gestion.buscar_por_codigo(codigo, gestion.pacientes)
                     or gestion.buscar_por_codigo(codigo, gestion.medicos)
                     or gestion.buscar_por_codigo(codigo, gestion.citas))
        print(resultado if resultado else "No se encontró ningún registro con ese código.")
        if not preguntar_continuar("buscar otro código"):
            break


def programar_cita_menu() -> None:
    while True:
        print("\n--- Programar cita ---")
        codigo_cita = input("Código nuevo para esta cita (ej. C010): ").strip()

        print("\nPacientes registrados:")
        for paciente_existente in gestion.pacientes:
            print(f"  {paciente_existente}")
        codigo_paciente = input("Código del paciente (ej. P001): ").strip()

        print("\nMédicos registrados:")
        for medico_existente in gestion.medicos:
            print(f"  {medico_existente}")
        codigo_medico = input("Código del médico (ej. M001): ").strip()

        fecha = input("Fecha de la cita (AAAA-MM-DD, ej. 2026-10-15): ").strip()
        try:
            cita = gestion.programar_cita(codigo_cita, codigo_paciente, codigo_medico, fecha)
            print(f"Cita creada: {cita}")
        except ValueError as error:
            print(f"Error: {error}")
        if not preguntar_continuar("programar una cita"):
            break


def registrar_atencion_menu() -> None:
    while True:
        print("Citas registradas:")
        cita_elegida = elegir_de_lista(gestion.citas, "No hay citas programadas todavía.")
        if cita_elegida is None:
            print("Operación cancelada: no hay ninguna cita para atender.")
        else:
            diagnostico = input("Diagnóstico ficticio (ej. Control de rutina): ").strip()
            observaciones = input("Observaciones (ej. Paciente estable): ").strip()
            try:
                cita = gestion.registrar_atencion(cita_elegida.codigo, diagnostico, observaciones)
                print(f"Atención registrada: {cita}")
            except ValueError as error:
                print(f"Error: {error}")
        if not preguntar_continuar("registrar una atención"):
            break


def buscar_especialidad_menu() -> None:
    while True:
        especialidad = elegir_especialidad()
        resultados = gestion.buscar_por_especialidad(especialidad)
        if resultados:
            for medico in resultados:
                print(medico)
        else:
            print("No hay médicos registrados con esa especialidad.")
        if not preguntar_continuar("buscar otra especialidad"):
            break


def consultar_historial_menu() -> None:
    while True:
        codigo_paciente = input("Código del paciente (ej. P001): ").strip()
        resultados = gestion.consultar_historial(codigo_paciente)
        if resultados:
            for cita in resultados:
                print(f"{cita} | Diagnóstico: {cita.diagnostico} | Observaciones: {cita.observaciones}")
        else:
            print("Ese paciente aún no tiene atenciones registradas.")
        if not preguntar_continuar("consultar otro historial"):
            break


def cargar_datos_iniciales() -> None:
    gestion.registrar_paciente("P001", "Ana Torres", "34")
    gestion.registrar_paciente("P002", "Luis Fernández", "45")
    gestion.registrar_paciente("P003", "Rosa Mamani", "28")
    gestion.registrar_paciente("P004", "Jorge Quispe", "60")

    gestion.registrar_medico("M001", "Carlos Ruiz", "Medicina general")
    gestion.registrar_medico("M002", "Elena Vargas", "Medicina general")
    gestion.registrar_medico("M003", "Marta Paredes", "Pediatría")
    gestion.registrar_medico("M004", "Pedro Salazar", "Pediatría")
    gestion.registrar_medico("M005", "Lucía Campos", "Obstetricia")
    gestion.registrar_medico("M006", "Diego Herrera", "Obstetricia")
    gestion.registrar_medico("M007", "Sofía Aranda", "Nutrición")
    gestion.registrar_medico("M008", "Miguel Ochoa", "Nutrición")
    gestion.registrar_medico("M009", "Valeria Rojas", "Odontología")
    gestion.registrar_medico("M010", "Andrés Flores", "Odontología")


def main() -> None:
    cargar_datos_iniciales()
    acciones = {
        "1": registrar_paciente_menu,
        "2": registrar_medico_menu,
        "3": buscar_por_codigo_menu,
        "4": programar_cita_menu,
        "5": registrar_atencion_menu,
        "6": buscar_especialidad_menu,
        "7": consultar_historial_menu,
    }
    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "0":
            break
        accion = acciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida.")
    print("Gracias por usar el Sistema Kawsay.")


if __name__ == "__main__":
    main()
