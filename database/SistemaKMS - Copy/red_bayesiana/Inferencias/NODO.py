class NODO:
    '''1.- Nodo virgen
    2.- Nodo subjetivo virgen
    3.- Nodo Objetivo
    4.- Nodo subjetivo
    5.- Nodo subjetivo lejano'''
    def __init__(self, id, clasificacion):
        self.id = id
        self.clasificacion = clasificacion
        self.ponderacion = 0
        self.sumatoria_ponderaciones = 0
        self.contador = 1
        self.grado_de_conocimiento = -1
        self.matriz_ponderacion = []  # MP
        self.matriz_inferencia = []  #
        self.matriz_inferencia_final = []  # i_prima

    def hola(self):
        print("Hello")

nodo = NODO("1", 2)
print(nodo.sumatoria_ponderaciones)