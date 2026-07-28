"""
Archivo     : pago.py
Descripción : Define la interfaz abstracta Pago y sus implementaciones
              concretas (tarjeta, efectivo, transferencia). Son los
              Productos que crean los Factory Methods y Abstract Factories.
Patrón GoF  : Factory Method – Producto (Creacional)
Curso       : Diseño de Patrones (UCA-IEP026)
Autores     : Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
              Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
Fecha       : 2026/07/2026
"""

from abc import ABC, abstractmethod

class Pago(ABC):
    @abstractmethod
    def procesar(self, monto: float) -> bool: pass

    @abstractmethod
    def tipo(self) -> str: pass

class PagoTarjeta(Pago):
    def __init__(self, numero: str):
        self._ultimos = numero[-4:]

    def procesar(self, monto: float) -> bool:
        print(f"[TARJETA ****{self._ultimos}] Procesando ${monto:.2f}")
        return True

    def tipo(self) -> str: return "tarjeta"

class PagoEfectivo(Pago):
    def procesar(self, monto: float) -> bool:
        print(f"[EFECTIVO] Registrando ${monto:.2f}")
        return True

    def tipo(self) -> str: return "efectivo"

class PagoTransferencia(Pago):
    def __init__(self, cuenta: str):
        self._cuenta = cuenta

    def procesar(self, monto: float) -> bool:
        print(f"[TRANSFERENCIA -> {self._cuenta}] ${monto:.2f}")
        return True

    def tipo(self) -> str: return "transferencia"