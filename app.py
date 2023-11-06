import tkinter as tk
import pickle
from modelo.existentesError import LibroExistenteError
from modelo.encontradoError import LibroNoEncontradoError
from modelo.biblioteca import Bibliotecas
from modelo.libro import Libro

def cargar_datos_predeterminados():
    try:
        with open('datos_libros.pkl', 'rb') as archivo:
            datos_libros = pickle.load(archivo)
            for datos in datos_libros:
                libro:Libro = Libro(datos["titulo"], datos["autor"], datos["isbn"])
                mi_biblioteca.agregar_libro(libro)
    except FileNotFoundError:
        pass  # El archivo aún no existe

def agregar_libro_desde_interfaz():
    titulo:str = titulo_entry.get()
    autor:str = autor_entry.get()
    isbn:int = isbn_entry.get()
    nuevo_libro:Libro = Libro(titulo, autor, isbn)
    try:
        resultado = mi_biblioteca.agregar_libro(nuevo_libro)
        resultado_label.config(text=resultado)
        listar_libros_desde_interfaz()
    except LibroExistenteError as e:
        resultado_label.config(text=str(e))

def eliminar_libro_desde_interfaz():
    titulo:str = titulo_eliminar_entry.get()
    try:
        resultado = mi_biblioteca.eliminar_libro(titulo)
        resultado_eliminar_label.config(text=resultado)
        lista_libros_text.config(text="")
    except LibroNoEncontradoError as e:
        resultado_eliminar_label.config(text=str(e))

def listar_libros_desde_interfaz():
    lista_libros_text.config(text=mi_biblioteca.listar_libros())

def mostrar_lista_libros():
    if lista_libros_text.cget("text") == "":
        listar_libros_desde_interfaz()
    else:
        lista_libros_text.config(text="")

root = tk.Tk()
root.title("Biblioteca Interactiva")

mi_biblioteca = Bibliotecas("Biblioteca Principal")

cargar_datos_predeterminados()

titulo_label = tk.Label(root, text="Título:")
autor_label = tk.Label(root, text="Autor:")
isbn_label = tk.Label(root, text="ISBN:")
resultado_label = tk.Label(root, text="", fg="green")
titulo_eliminar_label = tk.Label(root, text="Título del libro a eliminar:")
resultado_eliminar_label = tk.Label(root, text="", fg="green")
lista_libros_text = tk.Label(root, text="")
mostrar_lista_button = tk.Button(root, text="Mostrar/Esconder Lista", command=mostrar_lista_libros)

titulo_entry = tk.Entry(root)
autor_entry = tk.Entry(root)
isbn_entry = tk.Entry(root)
titulo_eliminar_entry = tk.Entry(root)

agregar_libro_button = tk.Button(root, text="Agregar Libro", command=agregar_libro_desde_interfaz)
eliminar_libro_button = tk.Button(root, text="Eliminar Libro", command=eliminar_libro_desde_interfaz)

titulo_label.grid(row=0, column=0)
autor_label.grid(row=1, column=0)
isbn_label.grid(row=2, column=0)
titulo_entry.grid(row=0, column=1)
autor_entry.grid(row=1, column=1)
isbn_entry.grid(row=2, column=1)
agregar_libro_button.grid(row=3, column=0, columnspan=2)
resultado_label.grid(row=4, column=0, columnspan=2)
titulo_eliminar_label.grid(row=5, column=0)
titulo_eliminar_entry.grid(row=5, column=1)
eliminar_libro_button.grid(row=6, column=0, columnspan=2)
resultado_eliminar_label.grid(row=7, column=0, columnspan=2)
mostrar_lista_button.grid(row=8, column=0, columnspan=2)
lista_libros_text.grid(row=9, column=0, columnspan=2)

root.mainloop()




