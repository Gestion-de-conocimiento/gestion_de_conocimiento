'''
1.- Nodo virgen
2.- Nodo subjetivo virgen
3.- Nodo Objetivo
4.- Nodo subjetivo
5.- Nodo subjetivo lejano    
'''
class NODO:
    def __init__(self, id, clasificacion):
        self.id = id
        self.clasificacion = clasificacion
        self.ponderacion = 0
        self.sumatoria_ponderaciones = 0
        self.contador = 1
        self.grado_de_conocimiento = -1
        self.matriz_ponderacion = [0,0,0]  # MP
        self.matriz_inferencia = [0,0,0]  # i_prima
        self.matriz_inferencia_final = [0,0,0]  # i_doble_prima
        self.dificultad = 0
        self.discriminacion = 0
        self.adivinacion = 0
        self.asintota = 0
        self.orden_evaluacion = -1
