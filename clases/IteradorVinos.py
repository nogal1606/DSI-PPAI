from typing import List
from InterfazIterador import InterfazIterador

class IteradorVinos(InterfazIterador):
    def __init__(self, elementos: List[object], filtros: List[object]):
        self.posicionActual
        self.elementos = elementos
        self.filtros = filtros
        
    def primero(self):
        self.posicionActual = 0
        
    def haTerminado(self):
        return self.actual == (len(self.elementos)-1)
    
    def siguiente(self):
        self.actual += 1
        
    def actual(self):
        if self.elementos[self.posicionActual].tenesResenasEnPeriodo:
            return self.elementos[self.posicionActual]
        return False