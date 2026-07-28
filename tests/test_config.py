import pytest
from src.config.configuracion import ConfiguracionApp

def test_singleton_retorna_misma_instancia():
    """Verifica que ConfiguracionApp implemente el patrón Singleton."""
    a = ConfiguracionApp()
    b = ConfiguracionApp()
    assert a is b

def test_singleton_mismos_valores():
    """Verifica que las instancias compartan los mismos atributos."""
    a = ConfiguracionApp()
    b = ConfiguracionApp()
    assert a.version == b.version
    assert a.entorno == b.entorno

def test_configuracion_tiene_version():
    """Verifica que exista el atributo de versión."""
    config = ConfiguracionApp()
    assert config.version == "1.0.0"

def test_es_produccion_por_defecto():
    """Verifica el comportamiento del entorno por defecto."""
    config = ConfiguracionApp()
    assert isinstance(config.es_produccion(), bool)