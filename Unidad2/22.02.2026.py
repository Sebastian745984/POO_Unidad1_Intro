############## Definicion de Clases ########################

class Libro:
  def __init__(self, isbn, titulo, autor, categoria, precio):
    self.isbn = isbn
    self.titulo = titulo
    self.autor = autor
    self.categoria = categoria
    self.precio = precio
    self.prestado = False
  def mostrar_info(self):
      estado = "Prestado" if self.prestado else "Disponible"
      print(f"[{self.isbn}] {self.titulo} - {self.autor} | {self.categoria} | ${self.precio} | {estado}")

class Estudiante:
  def __init__(self, num_control, nombre, carrera, fecha_nacimiento, telefono, correo):
      self.num_control = num_control
      self.nombre = nombre
      self.carrera = carrera
      self.fecha_nacimiento = fecha_nacimiento
      self.telefono = telefono
      self.correo = correo
  def mostrar_info(self):
      print(f"[{self.num_control}] {self.nombre} - {self.carrera} | Nac: {self.fecha_nacimiento} | Tel: {self.telefono} | Correo: {self.correo}")

class Prestamo:
      contador_prestamos = 1
      def __init__(self, num_control, isbn, fecha_inicio, fecha_termino):
        self.folio = Prestamo.contador_prestamos
        Prestamo.contador_prestamos += 1
        self.num_control = num_control
        self.isbn = isbn
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino

        def mostrar_info(self):
          print(f"Folio: {self.folio} | Estudiante: {self.num_control} | Libro: {self.libro} \
          Del {self.fecha_inicio} al {self.fecha_termino}")

