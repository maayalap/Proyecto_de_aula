class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = {}  # Un diccionario para almacenar libros

    def agregar_libro(self, libro) -> str:
        if libro.titulo in self.catalogo:
            print("El libro", "'", libro.titulo, "'", "ya está en el catálogo.")
        else:
            self.catalogo[libro.titulo] = libro
            print("Se ha agregado el libro", libro.titulo, "al catálogo.")

    def eliminar_libro(self, titulo) -> str:
        if titulo in self.catalogo:
            del self.catalogo[titulo]
            print("Se ha eliminado el libro", titulo, "del catálogo.")
        else:
            print("No se encontró el libro", titulo, "en el catálogo.")

    def listar_libros(self) -> str:
        if not self.catalogo:
            print("El catálogo de la biblioteca está vacío.")
        else:
            print("Libros en el catálogo de la biblioteca:")


class Libro:
    def __init__(self, titulo:str, autor:str, isbn:int):
        self.titulo:str = titulo
        self.autor:str = autor
        self.isbn:int = isbn

# Función para solicitar datos de un nuevo libro al usuario
def ingresar_nuevo_libro():
    titulo = input("Ingrese el título del nuevo libro: ")
    autor = input("Ingrese el autor del nuevo libro: ")
    isbn = input("Ingrese el ISBN del nuevo libro: ")
    return Libro(titulo, autor, isbn)

# Ejemplo de uso interactivo:
if __name__ == "__main__":
    mi_biblioteca = Biblioteca("Biblioteca Principal")

    while True:
        print("\nOpciones:")
        print("1. Agregar un nuevo libro")
        print("2. Eliminar un libro")
        print("3. Listar libros")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción que desee: ")

        if opcion == "1":
            nuevo_libro = ingresar_nuevo_libro()
            mi_biblioteca.agregar_libro(nuevo_libro)
        elif opcion == "2":
            titulo = input("Ingrese el título del libro que desea eliminar: ")
            mi_biblioteca.eliminar_libro(titulo)
        elif opcion == "3":
            mi_biblioteca.listar_libros()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

