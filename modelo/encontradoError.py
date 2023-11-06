class LibroNoEncontradoError(Exception):
    def __init__(self, titulo:str):
        self.titulo:str = titulo
        super().__init__(f"No se encontró el libro '{titulo}' en el catálogo.")