from typing import List
from PantallaExcel import PantallaExcel
from fpdf import FPDF
from IteradorVinos import IteradorVinos


class GestorRankingVinos:
    def __init__(self):
        # Atributos de la clase
        self.confirmacion = None
        self.pantalla = None  # Objeto de la clase Pantalla
        self.listaVinos = None  # Lista de objetos de la clase Vino
        self.fechaDesde = None  # DateTime
        self.fechaHasta = None  # DateTime
        self.infoVinos = []
        self.infoVinosOrdenados = None
        self.puntajeVinos = []
        self.tipoReportes = None
        self.tipoReporteSeleccionado = None
        self.tipoVisualizacion = None
        self.puntajeVinos = []
        self.pantallaExcel = None
        # puntero a la interfaz iterador - definirlo bien
        self.iteradorVinos = None
        
    def crearIterador(self, elementos: List[object], filtros: List[object]):
        self.iteradorVinos = IteradorVinos(elementos, filtros)

    def habilitarRanking(self):
        print("Habilitando ranking...")

    def opcionGenerarRankingVinos(self):
        # Se solicita el periodo para el ranking
        return self.pantalla.pedirSeleccionFechas()

    def obtenerInformacionVinoYReseñaEnPeriodo(self):
        self.crearIterador(self.listaVinos, [self.fechaDesde, self.fechaHasta])
        self.iteradorVinos.primero()
        while not self.iteradorVinos.haTerminado():
            if self.iteradorVinos.actual():
                # obtener datos de actual
                vino = self.iteradorVinos.actual()
                pass
            self.iteradorVinos.siguiente()
        
        for vino in self.listaVinos:
            if vino.tenesResenaDeTipoEnPeriodo(self.fechaDesde, self.fechaHasta):
                nombreVino = vino.getNombre()
                precioVino = vino.getPrecio()
                infoBodega = vino.buscarInfoBodega()
                if [nombreVino, precioVino, infoBodega] not in self.infoVinos:  # Check if the wine info is not already in the list
                    self.infoVinos.append([nombreVino, precioVino, infoBodega])
        
        
        return self.calcularPromedioResenasEnPeriodo()

    def setPantalla(self, pantalla):
        self.pantalla = pantalla

    def setVinos(self, lista_vinos):
        self.listaVinos = lista_vinos

    def tomarSeleccionFechaDesdeyHasta(self, fechaDesde, fechaHasta):
        self.fechaHasta = fechaHasta
        self.fechaDesde = fechaDesde
        return self.pantalla.solicitarTipoResena()

    def tomarSeleccionTipoResena(self, tipoReporte):
        self.tipoReporteSeleccionado = tipoReporte
        return self.pantalla.solicitarFormatoDelReporte()

    def tomarFormatoDelReporte(self, tipoVisualizacion):
        self.tipoVisualizacion = tipoVisualizacion
        return self.pantalla.solicitarConfirmacionReporte()

    def setTipoReportes(self, tipos):
        self.tipoReportes = tipos

    def tomarConfirmacionReporte(self, confirmacion):
        self.confirmacion = confirmacion
        return self.obtenerInformacionVinoYReseñaEnPeriodo()

    def setTipoVisualizacion(self, tipoVisualizacion):
        self.tipoVisualizacion = tipoVisualizacion

    def calcularPromedioResenasEnPeriodo(self):
        for vino in self.listaVinos:
            puntaje = vino.calcularPuntajeResenaEnPeriodo(self.fechaDesde, self.fechaHasta)
            self.puntajeVinos.append(puntaje)
        return self.ordenarVinosSegunPromedioPuntaje()

    def ordenarVinosSegunPromedioPuntaje(self):
        self.infoVinosOrdenados = [x for _, x in sorted(zip(self.puntajeVinos, self.infoVinos), reverse=True)]
        self.puntajeVinos.sort(reverse=True)
        if self.tipoVisualizacion == "PDF":
            return self.generarArchivoPDF(self.infoVinosOrdenados, self.puntajeVinos)
        return self.generarArchivoExcel(self.infoVinosOrdenados, self.puntajeVinos)

    def generarArchivoExcel(self, infoVinos, puntajeVinos):
        self.pantallaExcel = PantallaExcel(infoVinos, puntajeVinos)
        return self.finCU()

    def finCU(self):
        if self.tipoVisualizacion == "PDF":
            return self.pantalla.abrirPDF()
        elif self.tipoVisualizacion == "Excel":
            return self.pantallaExcel.abrirExcel(self.pantalla)
        return

    def generarArchivoPDF(self, infoVinos, puntajeVinos):
        print(infoVinos)
        contador = 0
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Encabezado
        pdf.cell(200, 10, txt="Ranking de Vinos", ln=True, align='C')

        # Tabla de vinos
        pdf.ln(10)
        pdf.set_font("Arial", size=10)
        pdf.cell(30, 10, txt="Nombre", border=1)
        pdf.cell(15, 10, txt="Precio", border=1)
        pdf.cell(53, 10, txt="Info Bodega", border=1)
        pdf.cell(45, 10, txt="Ubicacion Bodega", border=1)
        pdf.cell(41, 10, txt="Varietal", border=1)
        pdf.cell(14, 10, txt="Puntaje", border=1)
        pdf.ln(10)

        for vino in infoVinos:
            pdf.cell(30, 10, txt=vino[0], border=1)
            pdf.cell(15, 10, txt=str(vino[1]), border=1)
            pdf.cell(53, 10, txt=' ' + str(vino[2][0]), border=1)  # Unir los elementos de la lista en un string
            pdf.cell(45, 10, txt=' ' + str(vino[2][1]), border=1)  # Unir los elementos de la lista en un string
            pdf.cell(41, 10, txt=' ' + str(vino[2][2]), border=1)  # Unir los elementos de la lista en un string
            pdf.cell(14, 10, txt=str(puntajeVinos[contador]), border=1)
            pdf.ln(10)
            contador += 1

        # Guardar archivo PDF
        pdf.output("ranking_vinos.pdf", "F")
        print("Archivo PDF creado exitosamente.")
        return self.finCU()
