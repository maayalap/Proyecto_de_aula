class LibroExistenteError(Exception):
    def __init__(self, titulo:str):
        self.titulo:str = titulo
        super().__init__(f"El libro '{titulo}' ya está en el catálogo.")