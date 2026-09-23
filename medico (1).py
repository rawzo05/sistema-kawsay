class Medico:

    ESPECIALIDADES_VALIDAS = (
        "Medicina general",
        "Obstetricia",
        "Pediatría",
        "Nutrición",
        "Odontología",
    )

    def __init__(self, codigo: str, nombre: str, especialidad: str):
        self._codigo = str(codigo).strip().upper()
        self._nombre = nombre
        self._especialidad = especialidad

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self._nombre = valor

    @property
    def especialidad(self) -> str:
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor: str) -> None:
        self._especialidad = valor

    def __str__(self) -> str:
        return f"Medico[{self._codigo}] {self._nombre} - {self._especialidad}"
