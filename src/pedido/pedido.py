"""
Archivo     : pedido.py
Descripción : Modelo de dominio que representa un Pedido en el sistema.
              Es el producto que construye PedidoBuilder. Contiene la
              Lógica de cálculo de subtotal y total con descuento.
Patrón GoF  : Builder – Producto (Creacional)
Curso       : Diseño de Patrones (UCA-IEP026)
Autores     : Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
              Gabriel Herrera – 13497@ucarolina.edu.mx – 13497
Fecha       : 2026/07/2026
"""

class Pedido:
    def __init__(self):
        self.cliente = ""
        self.items = []  # lista de (nombre, precio, cantidad)
        self.direccion = ""
        self.descuento = 0.0
        self.notas = ""
        self.estado = "pendiente"
        self.numero = ""

    @property
    def subtotal(self) -> float:
        return sum(precio * cantidad for _, precio, cantidad in self.items)

    @property
    def total(self) -> float:
        return self.subtotal * (1 - self.descuento)

    def __str__(self):
        lineas = "\n ".join(
            f"{n}: ${p:.2f} x{c}" for n, p, c in self.items
        )
        return (
            f"Pedido #{self.numero} – {self.cliente}\n"
            f" {lineas}\n"
            f" Dirección: {self.direccion}\n"
            f" Descuento: {self.descuento*100:.0f}%\n"
            f" Total: ${self.total:.2f}\n"
            f" Estado: {self.estado}"
        )