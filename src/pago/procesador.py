"""
Archivo     : procesador.py
Descripción : Define ProcesadorPago como Creator abstracto con el Factory
              Method crear_pago(). Cada subclase concreta decide qué tipo
              de Pago instanciar. Incluye función fábrica como variante
              simple.
Patrón GoF  : Factory Method – Creator (Creacional)
Curso       : Diseño de Patrones (UCA-IEP026)
Autores     : Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
              Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
Fecha       : 2026/07/2026
"""

from abc import ABC, abstractmethod
from src.pago.pago import Pago, PagoTarjeta, PagoEfectivo, PagoTransferencia

class ProcesadorPago(ABC):

    @abstractmethod
    def crear_pago(self) -> Pago: pass  # ← Factory Method

    def pagar(self, monto: float) -> bool:
        pago = self.crear_pago()
        print(f"Iniciando pago via {pago.tipo()}...")
        return pago.procesar(monto)

class ProcesadorTarjeta(ProcesadorPago):
    def __init__(self, numero: str):
        self._numero = numero

    def crear_pago(self) -> Pago:
        return PagoTarjeta(self._numero)

class ProcesadorEfectivo(ProcesadorPago):
    def crear_pago(self) -> Pago:
        return PagoEfectivo()

class ProcesadorTransferencia(ProcesadorPago):
    def __init__(self, cuenta: str):
        self._cuenta = cuenta

    def crear_pago(self) -> Pago:
        return PagoTransferencia(self._cuenta)

def crear_procesador(tipo: str, **kwargs) -> ProcesadorPago:
    """Función fábrica – alternativa simple sin jerarquía de Creator"""
    opciones = {
        "tarjeta":       lambda: ProcesadorTarjeta(kwargs["numero"]),
        "efectivo":      lambda: ProcesadorEfectivo(),
        "transferencia": lambda: ProcesadorTransferencia(kwargs["cuenta"]),
    }
    if tipo not in opciones:
        raise ValueError(f"Tipo de pago desconocido: '{tipo}'")
    return opciones[tipo]()