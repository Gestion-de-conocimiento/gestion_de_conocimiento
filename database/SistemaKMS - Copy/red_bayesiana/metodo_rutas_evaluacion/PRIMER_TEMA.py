import requests
import random

class PRIMER_TEMA:

    def __init__(self, caminosModulo):
        self.caminos = caminosModulo['caminos']
        self.temas = caminosModulo['temas']

    def elegirTema(self, lista):
            tamanioLista = len(lista)
            totalElementosARetirar = int( tamanioLista / 3 )
            if tamanioLista > 2:
                lista = lista[totalElementosARetirar::]
                lista = lista[:-totalElementosARetirar]

            return random.choice(lista)

    def calcularPrimerTema(self):
        # Saber cuales son los nodos rama y area disciplinar
        temasRamas = []
        for tema in self.temas:
            if tema['nivel'] < 2:
                temasRamas.append(tema['id'])

        # Obener el camino que pasa por todos los nodos que son ramas
        temasRamasEnOrden = []
        for camino in self.caminos:
            contieneRamas = all(item in camino for item in temasRamas)
            if contieneRamas:
                for nodo in camino:
                    for n in temasRamas:
                        if n == nodo:
                            temasRamasEnOrden.append(n)
                            break

        temasRamasEnOrden = temasRamasEnOrden[1:]
        temaSeleccionado = self.elegirTema( temasRamasEnOrden )
        temasPosibles = []
        for camino in self.caminos:
            for i in range(len(camino)):
                if camino[i] == temaSeleccionado and not(camino[i+1] in temasRamasEnOrden):
                    temasPosibles = temasPosibles + camino[i+1:]
                    exit

        return random.choice(list(dict.fromkeys(temasPosibles)))
