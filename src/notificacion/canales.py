"""
Archivo     : canales.py
Descripción : Define la jerarquía de Implementadores (Implementor) del patrón
              Bridge. Cada Canal encarga cómo se entrega físicamente un
              mensaje: por email, SMS o consola. Las abstracciones no conocen
              los detalles de ningún canal específico.
Patrón GoF  : Bridge – Implementor (Estructural)
Curso       : Diseño de Patrones (UCA-IEP026)
Autores     : Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
              Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
Fecha       : 2026/07/2026
"""

from abc import ABC, abstractmethod

class Canal(ABC):
    @abstractmethod
    def enviar(self, destinatario: str, texto: str) -> None: pass

class CanalEmail(Canal):
    def enviar(self, destinatario, texto):
        print(f"[EMAIL → {destinatario}] {texto}")

class CanalSMS(Canal):
    def enviar(self, destinatario, texto):
        print(f"[SMS → {destinatario}] {texto}")

class CanalConsola(Canal):
    """Útil para pruebas y logging interno"""
    def enviar(self, destinatario, texto):
        print(f"[LOG] {destinatario}: {texto}")