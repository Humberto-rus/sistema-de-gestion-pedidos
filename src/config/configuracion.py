"""
Archivo     : configuracion.py
Descripción : Configuración global de la aplicación usando el patrón
              Singleton.
              Garantiza que solo exista una instancia de ConfiguracionApp
              en todo el ciclo de vida del proceso.
Patrón GoF  : Singleton (Creacional)
Curso       : Diseño de Patrones (UCA-IEP026)
Autores     : Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
              Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
Fecha       : 2026
"""

import os

class ConfiguracionApp:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.entorno = os.getenv("ENTORNO", "produccion")
            cls._instancia.version = "1.0.0"
            cls._instancia.debug = os.getenv("DEBUG", "false") == "true"
        return cls._instancia

    def es_produccion(self) -> bool:
        return self.entorno == "produccion"

    def __str__(self):
        return f"Config(entorno={self.entorno}, version={self.version})"