"""
Archivo     : factory.py
Descripción : Implementa el patrón Abstract Factory para la creación de
              pasarelas de pago. PasarelaProduccion crea objetos reales;
              PasarelaPruebas crea mocks que no realizan cargos. La función
              obtener_pasarela() selecciona la familia según la variable
              de entorno ENTORNO.
Patrón GoF  : Abstract Factory (Creacional)
Curso       : Diseño de Patrones (UCA-IEP026)
Autores     : Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
              Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
Fecha       : 2026/07/2026
"""

import os
from abc import ABC, abstractmethod
from src.pago.pago import Pago, PagoTarjeta, PagoEfectivo

class PagoMock(Pago):
    """Producto mock – nunca realiza cargos reales"""
    def __init__(self, etiqueta: str = "mock"):
        self._etiqueta = etiqueta

    def procesar(self, monto: float) -> bool:
        print(f"[MOCK] Simulando ${monto:.2f} – sin cargo real")
        return True

    def tipo(self) -> str: return f"mock-{self._etiqueta}"

class PasarelaPago(ABC):
    @abstractmethod
    def crear_pago_tarjeta(self, numero: str) -> Pago: pass

    @abstractmethod
    def crear_pago_efectivo(self) -> Pago: pass

class PasarelaProduccion(PasarelaPago):
    def crear_pago_tarjeta(self, numero: str) -> Pago:
        return PagoTarjeta(numero)

    def crear_pago_efectivo(self) -> Pago:
        return PagoEfectivo()

class PasarelaPruebas(PasarelaPago):
    def crear_pago_tarjeta(self, numero: str) -> Pago:
        return PagoMock("tarjeta")

    def crear_pago_efectivo(self) -> Pago:
        return PagoMock("efectivo")

def obtener_pasarela() -> PasarelaPago:
    entorno = os.getenv("ENTORNO", "produccion")
    return PasarelaPruebas() if entorno == "pruebas" else PasarelaProduccion()