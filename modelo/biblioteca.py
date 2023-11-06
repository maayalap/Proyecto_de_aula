import pickle
from modelo.encontradoError import LibroNoEncontradoError
from modelo.existentesError import LibroExistenteError

# Datos de los libros predeterminados
libro1 = {"titulo": "El varon domado", "autor": "Esther Vilar", "isbn": 123}
libro2 = {"titulo": "Las 48 leyes del poder", "autor": "Robert Greene", "isbn": 456}
libro3 = {"titulo": "Psicología oscura", "autor": "Steven Turner", "isbn": 789}

# Almacena los datos en el archivo 'datos_libros.pkl'
datos_libros = [libro1, libro2, libro3]
with open('datos_libros.pkl', 'wb') as archivo:
    pickle.dump(datos_libros, archivo)

class Bibliotecas:
    def __init__(self, nombre:str):
        self.nombre:str = nombre
        self.catalogo:dict = {}  # Un diccionario para almacenar libros

    def agregar_libro(self, libro):
        if libro.titulo in self.catalogo:
            raise LibroExistenteError(libro.titulo)
        else:
            self.catalogo[libro.titulo] = libro
            return "Se ha agregado el libro '" + libro.titulo + "' al catálogo."

    def eliminar_libro(self, titulo):
        if titulo in self.catalogo:
            del self.catalogo[titulo]
            return "Se ha eliminado el libro '" + titulo + "' del catálogo."
        else:
            raise LibroNoEncontradoError(titulo)

    def listar_libros(self):
        if not self.catalogo:
            return "El catálogo de la biblioteca está vacío."
        else:
            libros = [f"- '{titulo}' de {libro.autor}" for titulo, libro in self.catalogo.items()]
            return "\n".join(libros)


            