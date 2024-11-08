class Bodega:
    def __init__(self, descripcion, nombre, region):
        self.descripcion = descripcion
        self.nombre = nombre
        self.region = region

    def getNombre(self):
        return self.nombre
    
    def obtenerRegionYPais(self):
        nombreRegion = self.region.getNombre()
        nombrePais = self.region.obtenerPais()
        return [nombreRegion, nombrePais]
