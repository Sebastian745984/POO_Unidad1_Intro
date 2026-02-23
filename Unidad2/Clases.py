
class Venta:
  contador_ventas = 1
  def __init__(self, isbn, num_control, fecha, cantidad, importe):
    self.folio_ventas = Venta.contador_ventas
    Venta.contador_ventas += 1
    self.isbn = isbn
    self.num_control = num_control
    self.fecha = fecha
    self.cantidad = cantidad
    self.importe = importe

    def mostrar_info(self):
      print(f"Folio: {self.folio_ventas} | ISBN: {self.isbn} | Comprador: {self.num_control} | \
        Fecha: {self.fecha} | Cantidad: {self.cantidad} | Importe{self.importe}")

