class Vino:
    def __init__(self, añada, imagenEtiqueta, nombre, notaDeCataBodega, precioARS, bodega, varietal):
        self.añada = añada
        self.imagenEtiqueta = imagenEtiqueta
        self.nombre = nombre
        self.notaDeCataBodega = notaDeCataBodega
        self.precioARS = precioARS
        self.bodega = bodega
        self.varietales = varietal
        self.resenias = []

    # Getter for añada
    def getAñada(self):
        return self.añada

    # Setter for añada
    def setAñada(self, añada):
        self.añada = añada

    # Getter for imagenEtiqueta
    def getImagenEtiqueta(self):
        return self.imagenEtiqueta

    # Setter for imagenEtiqueta
    def setImagenEtiqueta(self, imagenEtiqueta):
        self.imagenEtiqueta = imagenEtiqueta

    # Getter for nombre
    def getNombre(self):
        return self.nombre

    # Setter for nombre
    def setNombre(self, nombre):
        self.nombre = nombre

    # Getter for notaDeCataBodega
    def getNotaDeCataBodega(self):
        return self.notaDeCataBodega

    # Setter for notaDeCataBodega
    def setNotaDeCataBodega(self, notaDeCataBodega):
        self.notaDeCataBodega = notaDeCataBodega

    # Getter for precioARS
    def getPrecio(self):
        return self.precioARS

    # Setter for precioARS
    def setPrecio(self, precioARS):
        self.precioARS = precioARS

    # Getter for bodega
    def getBodega(self):
        return self.bodega

    # Setter for bodega
    def setBodega(self, bodega):
        self.bodega = bodega

    # Getter for varietal
    def getVarietal(self):
        return self.varietal

    # Setter for varietal
    def setVarietal(self, varietal):
        self.varietales = varietal

    # Getter for resenias
    def getResenias(self):
        return self.resenias

    # Setter for resenias
    def setResenias(self, resenias):
        self.resenias = resenias

    def tenesResenaDeTipoEnPeriodo(self, fechaDesde, fechaHasta):
        for resenia in self.resenias:
            if resenia.sosDePeriodo(fechaDesde, fechaHasta) and resenia.sosResenaPremium():
                return True
        return False

    def buscarInfoBodega(self):
        nombreBodega = self.bodega.getNombre()
        nombrePais = self.bodega.obtenerRegionYPais()
        descripcionVarietal = []
        for varietal in self.varietales:
            descripcionVarietal.append(varietal.getDescripcion())
        return [nombreBodega, nombrePais, descripcionVarietal]

    def calcularPuntajeResenaEnPeriodo(self, fechaDesde, fechaHasta):
        puntajeAcumulado = 0
        contadorResenas = 0
        for resena in self.resenias:
            print(fechaDesde, fechaHasta)
            if resena.sosDePeriodo(fechaDesde, fechaHasta) and resena.sosResenaPremium():
                puntajeAcumulado += resena.getPuntaje()
                contadorResenas += 1
        if contadorResenas > 0:
            return self.calcularPromedio(contadorResenas, puntajeAcumulado)
        return 0

    def calcularPromedio(self, contador, puntajeAcumulado):
        promedio = puntajeAcumulado / contador
        return promedio
