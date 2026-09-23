from paciente import Paciente
from medico import Medico


class Cita:

    def __init__(self, codigo: str, paciente: Paciente, medico: Medico, fecha: str):
        self._codigo = str(codigo).strip().upper()
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._diagnostico = None
        self._observaciones = None
        self._atendida = False

    @property
    def codigo(self) -> str:
        return self._codigo


    @property
    def paciente(self) -> Paciente:
        return self._paciente

    @property
    def medico(self) -> Medico:
        return self._medico

    @property
    def fecha(self) -> str:
        return self._fecha

    @fecha.setter
    def fecha(self, valor: str) -> None:
        self._fecha = valor

    @property
    def diagnostico(self):
        return self._diagnostico

    @property
    def observaciones(self):
        return self._observaciones

    @property
    def atendida(self) -> bool:
        return self._atendida

    def registrar_atencion(self, diagnostico: str, observaciones: str) -> None:
        self._diagnostico = diagnostico
        self._observaciones = observaciones
        self._atendida = True

    def __str__(self) -> str:
        estado = "Atendida" if self._atendida else "Programada"
        return (f"Cita[{self._codigo}] {self._paciente.nombre} con "
                f"{self._medico.nombre} el {self._fecha} - {estado}")
