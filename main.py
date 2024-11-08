import tkinter as tk
#Importamos Clases a usar
from clases.Bodega import Bodega
from clases.Pais import Pais
from clases.PantallaRankingVinos import PantallaRankingVinos
from clases.Varietal import Varietal
from clases.RegionVitivinicola import RegionVitivinicola
from clases.GestorRankingVinos import GestorRankingVinos
from clases.Provincia import Provincia
from clases.Vino import Vino


def main():
     # Declaramos una lista de vinos de ejemplo
     listaVinos = [
          Vino(añada=2005, imagenEtiqueta="https://example.com/etiqueta1.jpg", nombre="Vino 1",
               notaDeCataBodega="Nota de cata 1", precioARS=3589.0, bodega=Bodega("Bodega 250", "Catena Zapata",
                                                                                     RegionVitivinicola("Valle de Uco",
                                                                                                    Provincia("Mendoza",
                                                                                                              Pais(
                                                                                                                   "Argentina")))),
               varietal=Varietal("Tempranillo")),
          Vino(añada=2018, imagenEtiqueta="https://example.com/etiqueta2.jpg", nombre="Vino 2",
               notaDeCataBodega="Nota de cata 2", precioARS=2773.0, bodega=Bodega("Bodega 150", "Trapiche",
                                                                                     RegionVitivinicola("Valle de Uco",
                                                                                                    Provincia("Mendoza",
                                                                                                              Pais(
                                                                                                                   "Argentina")))),
               varietal=Varietal("Merlot")),
          Vino(añada=2006, imagenEtiqueta="https://example.com/etiqueta3.jpg", nombre="Vino 3",
               notaDeCataBodega="Nota de cata 3", precioARS=4382.0, bodega=Bodega("Bodega 20", "Bodegas Muga",
                                                                                     RegionVitivinicola("Rioja Alta",
                                                                                                    Provincia("La Rioja",
                                                                                                              Pais(
                                                                                                                   "España")))),
               varietal=Varietal("Cabernet Sauvignon")),
          Vino(añada=2013, imagenEtiqueta="https://example.com/etiqueta4.jpg", nombre="Vino 4",
               notaDeCataBodega="Nota de cata 4", precioARS=4807.0,
               bodega=Bodega("Bodega 10", "Domaine de la Romanée-Conti",
                              RegionVitivinicola("Côte de Nuits", Provincia("Borgoña", Pais("Francia")))),
               varietal=Varietal("Pinot Noir")),
          Vino(añada=2008, imagenEtiqueta="https://example.com/etiqueta5.jpg", nombre="Vino 5",
               notaDeCataBodega="Nota de cata 5", precioARS=3512.0, bodega=Bodega("Bodega 1", "Marchesi Antinori",
                                                                                     RegionVitivinicola("Chianti",
                                                                                                    Provincia("Toscana",
                                                                                                              Pais(
                                                                                                                   "Italia")))),
               varietal=Varietal("Malbec")),
          Vino(añada=2015, imagenEtiqueta="https://example.com/etiqueta6.jpg", nombre="Vino 6",
               notaDeCataBodega="Nota de cata 6", precioARS=3961.0, bodega=Bodega("Bodega 2", "Viña Montes",
                                                                                     RegionVitivinicola("Pedernal",
                                                                                                    Provincia("San Juan",
                                                                                                              Pais(
                                                                                                                   "Argentina")))),
               varietal=Varietal("Tempranillo")),
          Vino(añada=2007, imagenEtiqueta="https://example.com/etiqueta7.jpg", nombre="Vino 7",
               notaDeCataBodega="Nota de cata 7", precioARS=2694.0, bodega=Bodega("Bodega 3", "Concha y Toro",
                                                                                     RegionVitivinicola("Pedernal",
                                                                                                    Provincia("San Juan",
                                                                                                              Pais(
                                                                                                                   "Argentina")))),
               varietal=Varietal("Cabernet Sauvignon")),
          Vino(añada=2002, imagenEtiqueta="https://example.com/etiqueta8.jpg", nombre="Vino 8",
               notaDeCataBodega="Nota de cata 8", precioARS=1345.0, bodega=Bodega("Bodega 4", "Bodegas Muga",
                                                                                     RegionVitivinicola("Rioja Alta",
                                                                                                    Provincia("La Rioja",
                                                                                                              Pais(
                                                                                                                   "España")))),
               varietal=Varietal("Tempranillo")),
          Vino(añada=2017, imagenEtiqueta="https://example.com/etiqueta9.jpg", nombre="Vino 9",
               notaDeCataBodega="Nota de cata 9", precioARS=4485.0, bodega=Bodega("Bodega 5", "Catena Zapata",
                                                                                     RegionVitivinicola("Valle de Uco",
                                                                                                    Provincia("Mendoza",
                                                                                                              Pais(
                                                                                                                   "Argentina")))),
               varietal=Varietal("Merlot")),
          Vino(añada=2011, imagenEtiqueta="https://example.com/etiqueta10.jpg", nombre="Vino 10",
               notaDeCataBodega="Nota de cata 10", precioARS=4756.0, bodega=Bodega("Bodega 6", "Trapiche",
                                                                                     RegionVitivinicola("Valle de Uco",
                                                                                                         Provincia("Mendoza",
                                                                                                                   Pais(
                                                                                                                   "Argentina")))),
               varietal=Varietal("Pinot Noir")),
          Vino(añada=2009, imagenEtiqueta="https://example.com/etiqueta11.jpg", nombre="Vino 11",
               notaDeCataBodega="Nota de cata 11", precioARS=1223.0, bodega=Bodega("Bodega 7", "Marchesi Antinori",
                                                                                     RegionVitivinicola("Chianti",
                                                                                                         Provincia("Toscana",
                                                                                                                   Pais(
                                                                                                                   "Italia")))),
               varietal=Varietal("Cabernet Sauvignon")),
          Vino(añada=2003, imagenEtiqueta="https://example.com/etiqueta12.jpg", nombre="Vino 12",
               notaDeCataBodega="Nota de cata 12", precioARS=4422.0, bodega=Bodega("Bodega 8", "Concha y Toro",
                                                                                     RegionVitivinicola("Pedernal",
                                                                                                         Provincia(
                                                                                                         "San Juan",
                                                                                                         Pais(
                                                                                                              "Argentina")))),
               varietal=Varietal("Malbec")),
          Vino(añada=2014, imagenEtiqueta="https://example.com/etiqueta13.jpg", nombre="Vino 13",
               notaDeCataBodega="Nota de cata 13", precioARS=4034.0, bodega=Bodega("Bodega 9", "Bodegas Muga",
                                                                                     RegionVitivinicola("Rioja Alta",
                                                                                                         Provincia(
                                                                                                         "La Rioja",
                                                                                                         Pais(
                                                                                                              "España")))),
               varietal=Varietal("Tempranillo")),
          Vino(añada=2000, imagenEtiqueta="https://example.com/etiqueta14.jpg", nombre="Vino 14",
               notaDeCataBodega="Nota de cata 14", precioARS=1442.0, bodega=Bodega("Bodega 11", "Catena Zapata",
                                                                                     RegionVitivinicola("Valle de Uco",
                                                                                                         Provincia("Mendoza",
                                                                                                                   Pais(
                                                                                                                   "Argentina")))),
               varietal=Varietal("Pinot Noir")),
          Vino(añada=2001, imagenEtiqueta="https://example.com/etiqueta15.jpg", nombre="Vino 15",
               notaDeCataBodega="Nota de cata 15", precioARS=4555.0, bodega=Bodega("Bodega 452", "Viña Montes",
                                                                                     RegionVitivinicola("Pedernal",
                                                                                                         Provincia(
                                                                                                         "San Juan",
                                                                                                         Pais(
                                                                                                              "Argentina")))),
               varietal=Varietal("Cabernet Sauvignon")),
          Vino(añada=2016, imagenEtiqueta="https://example.com/etiqueta16.jpg", nombre="Vino 16",
               notaDeCataBodega="Nota de cata 16", precioARS=4134.0, bodega=Bodega("Bodega 456", "Marchesi Antinori",
                                                                                     RegionVitivinicola("Chianti",
                                                                                                         Provincia("Toscana",
                                                                                                                   Pais(
                                                                                                                   "Italia")))),
               varietal=Varietal("Merlot")),
          Vino(añada=2012, imagenEtiqueta="https://example.com/etiqueta17.jpg", nombre="Vino 17",
               notaDeCataBodega="Nota de cata 17", precioARS=3752.0, bodega=Bodega("Bodega 453", "Concha y Toro",
                                                                                     RegionVitivinicola("Pedernal",
                                                                                                         Provincia(
                                                                                                         "San Juan",
                                                                                                         Pais(
                                                                                                              "Argentina")))),
               varietal=Varietal("Malbec")),
          Vino(añada=2004, imagenEtiqueta="https://example.com/etiqueta18.jpg", nombre="Vino 18",
               notaDeCataBodega="Nota de cata 18", precioARS=3076.0,
               bodega=Bodega("Bodega 45", "Domaine de la Romanée-Conti",
                              RegionVitivinicola("Côte de Nuits", Provincia("Borgoña", Pais("Francia")))),
               varietal=Varietal("Tempranillo")),
          Vino(añada=2010, imagenEtiqueta="https://example.com/etiqueta19.jpg", nombre="Vino 19",
               notaDeCataBodega="Nota de cata 19", precioARS=2543.0, bodega=Bodega("Bodega 789", "Trapiche",
                                                                                     RegionVitivinicola("Valle de Uco",
                                                                                                         Provincia("Mendoza",
                                                                                                                   Pais(
                                                                                                                   "Argentina")))),
               varietal=Varietal("Cabernet Sauvignon")),
          Vino(añada=2009, imagenEtiqueta="https://example.com/etiqueta20.jpg", nombre="Vino 20",
               notaDeCataBodega="Nota de cata 20", precioARS=4195.0, bodega=Bodega("Bodega 89", "Bodegas Muga",
                                                                                     RegionVitivinicola("Rioja Alta",
                                                                                                         Provincia(
                                                                                                         "La Rioja",
                                                                                                         Pais(
                                                                                                              "España")))),
               varietal=Varietal("Cabernet Sauvignon"))
     ]

     # Creamos un Gestor y una panatalla y los seteaamos mutuamente
     gestor = GestorRankingVinos()
     pantalla = PantallaRankingVinos()

     gestor.setVinos(listaVinos)

     # Seteamos el gestor y la pantalla mutuamente
     gestor.setPantalla(pantalla)
     pantalla.setGestor(gestor)

     # Inicializamos la pantalla
     pantalla.opcionGenerarRanking()



if __name__ == "__main__":
    main()
