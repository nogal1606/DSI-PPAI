class RegionVitivinicola:
    def __init__(self, nombre, provincia):
        self.nombre = nombre
        self.provincia = provincia
        
    def getNombre(self):
        return self.nombre

    def obtenerPais(self):
        return self.provincia.obtenerPais()