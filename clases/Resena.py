class Resena:
    def __init__(self, comentario, fechaResena, puntaje):
        self.comentario = comentario
        self.esPremium = True
        self.fechaResena = fechaResena
        self.puntaje = puntaje

    #Metodos get and set
    def get_comentario(self):
        return self.comentario

    def set_comentario(self, comentario):
        self.comentario = comentario

    def get_esPremium(self):
        return self.esPremium

    def set_esPremium(self, esPremium):
        self.esPremium = esPremium

    def get_fechaResena(self):
        return self.fechaResena

    def set_fechaResena(self, fechaResena):
        self.fechaResena = fechaResena

    def getPuntaje(self):
        return self.puntaje

    def set_puntaje(self, puntaje):
        self.puntaje = puntaje

    def sosDePeriodo(self, fechaDesde, fechaHasta):
        print(self.fechaResena)
        return fechaDesde <= self.fechaResena <= fechaHasta

    def sosResenaPremium(self):
        return self.esPremium
