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


     

def alta_libro():
    print("\n--- ALTA DE LIBRO ---")
    isbn = input("ISBN: ")
    for libro in libros:
      if libro.isbn == isbn:
        print("El libro ya existe con ese ISBN")
        return
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    categoria = input("Categoria: ")
    try:
        precio = float(input("Precio: "))
    except ValueError:
      print("Precio Invalido")
      return
    nuevo_libro = Libro(isbn, titulo, autor, categoria, precio)
    libros.append(nuevo_libro)
    print("Libro dado de alta correctamente")

     

def alta_estudiante():
  print("\n -- Alta de estudiante ---")
  num_control = input("Numero de control: ")
  for est in estudiantes:
    if est.num_control == num_control:
      print("El estudiante ya existe con ese numero de control")
      return
  nombre = input("Nombre: ")
  carrera = input("Carrera: ")
  fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
  telefono = input("Telefono: ")
  correo = input("Correo: ")
  nuevo_estudiante = Estudiante(num_control, nombre, carrera, fecha_nacimiento, telefono, correo)
  estudiantes.append(nuevo_estudiante)
  print("Estudiante dado de alta correctamente")
     


     


     

def mostrar_menu():
  print("\n--- SISTEMA DE LIBRERIA ESCOLAR ---")
  print("1. Dar de alta un Libro")
  print("2. Dar de alta estudiante")
  print("3. Colsultar libro por ISBN")
  print("4. Consultar estudiante por numero de control")
  print("5. Mostrar todos los libros")
  print("6. Mostrar todos los estudiantes")
  print("7. Realizar prestamo")
  print("8. Mostrar prestamos")
  print("9. Devolver libro")
  print("10. Registrar ventas")
  print("11. Mostrar historial de Ventas")
  print("12. Salir del sistema")

def: iniciar_sistema():
while True:
      mostrar_menu()
      opcion = input("Seleccione una opcion: ")
      if opcion == 1:
        alta_libro()
      elif opcion == 2:
        alta_estudiante()
      elif opcion == 3:
          consultar_libro()
      elif opcion == 4:
          consultar_estudiante()
      elif opcion == 5:
          mostrar_todos_libros()
      elif opcion == 6:
          mostrar_todos_estudiantes()
      elif opcion == 7:
          realizar_prestamo()
      elif opcion == 8:
          mostrar_prestamos()
      elif opcion == 9:
          devolver_libro()
      elif opcion == 10:
          registrar_venta()
      elif opcion == 11:
          mostrar_historial_ventas()
      elif opcion == 12:
          print("Saliendo del sistema...")
          break
      else:
        print("Opcion invalida. Intente de nuevo")
