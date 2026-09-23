class Paciente:

    def __init__(self, codigo: str, nombre: str, edad: int):
        self._codigo = str(codigo).strip().upper()
        self._nombre = nombre
        self._edad = edad

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
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, valor: int) -> None:
        self._edad = valor

    def __str__(self) -> str:
        return f"Paciente[{self._codigo}] {self._nombre}, {self._edad} años"
