import pyAgrum as gum
import numpy as numpy

class MPCN:
    def __init__(self, NODOS, SRB, caminos_ordenados, tema_objetivo, ponderacion_objetiva, RBM_nombre):
        self.NODOS = NODOS
        self.SRB = SRB
        self.caminos_ordenados = caminos_ordenados
        self.tema_objetivo = str(tema_objetivo)
        self.ponderacion_objetiva = ponderacion_objetiva
        self.RBM_nombre = RBM_nombre

    def ponderarNodos(self):
      
        orden_evaluados=-1
        for nodo in self.NODOS:
            if self.NODOS[nodo].orden_evaluacion != -1:
                orden_evaluados=orden_evaluados+1

        self.NODOS[self.tema_objetivo].ponderacion = self.ponderacion_objetiva
        self.NODOS[self.tema_objetivo].orden_evaluacion = orden_evaluados + 1
        self.NODOS[self.tema_objetivo].clasificacion = 3
        
        for camino in self.caminos_ordenados['abajo']:
            ponderacion = self.ponderacion_objetiva
            saltos = 1
            for nodo in camino:
                nodo_str = str(nodo)
                ponderacion = ponderacion * 0.5
                
                if self.NODOS[nodo_str].clasificacion != 3:
                    if saltos > 3:
                        if self.NODOS[nodo_str].clasificacion != 4:
                            self.NODOS[nodo_str].clasificacion = 5
                            self.NODOS[nodo_str].ponderacion = 2
                            self.NODOS[nodo_str].sumatoria_ponderaciones = 0
                    else:
                        if self.NODOS[nodo_str].clasificacion == 5:
                            self.NODOS[nodo_str].sumatoria_ponderaciones = ponderacion
                            self.NODOS[nodo_str].contador = 1
                        else:
                            self.NODOS[nodo_str].sumatoria_ponderaciones = self.NODOS[nodo_str].sumatoria_ponderaciones + ponderacion

                        self.NODOS[nodo_str].ponderacion = self.NODOS[nodo_str].sumatoria_ponderaciones / self.NODOS[nodo_str].contador
                        self.NODOS[nodo_str].clasificacion = 4
                        self.NODOS[nodo_str].contador = self.NODOS[nodo_str].contador + 1
                    saltos = saltos + 1

        for camino in self.caminos_ordenados['arriba']:
            ponderacion = self.ponderacion_objetiva
            for nodo in camino:
                nodo_str = str(nodo)
                ponderacion = ponderacion * 1.25
                if ponderacion > 100:
                    ponderacion = 100
                    
                if self.NODOS[nodo_str].clasificacion != 3:
                    self.NODOS[nodo_str].clasificacion = 4
                    self.NODOS[nodo_str].sumatoria_ponderaciones = self.NODOS[nodo_str].sumatoria_ponderaciones + ponderacion
                    self.NODOS[nodo_str].ponderacion = self.NODOS[nodo_str].sumatoria_ponderaciones / self.NODOS[nodo_str].contador
                    self.NODOS[nodo_str].contador = self.NODOS[nodo_str].contador + 1
         
        # Actualizar la RBMA con el resultado del método de ponderación de nodos
        for nodo in self.SRB.nodes():
            nodoSRB = self.SRB.variable(nodo).name()
            
            #Resetear la matriz de ponderación
            self.NODOS[nodoSRB].matriz_ponderacion = [0,0,0] 
            if self.NODOS[nodoSRB].ponderacion >= 0.0 and self.NODOS[nodoSRB].ponderacion <= 66.0:
                self.NODOS[nodoSRB].matriz_ponderacion[0] = 100
                self.NODOS[nodoSRB].grado_de_conocimiento = 0
            elif self.NODOS[nodoSRB].ponderacion > 66.0 and self.NODOS[nodoSRB].ponderacion <= 83.0:
                self.NODOS[nodoSRB].matriz_ponderacion[1] = 100
                self.NODOS[nodoSRB].grado_de_conocimiento = 1
            else:
                self.NODOS[nodoSRB].matriz_ponderacion[2] = 100
                self.NODOS[nodoSRB].grado_de_conocimiento = 2

    def hacerInferencias(self):
      
        self.ponderarNodos()
      
        RB = gum.loadBN( self.RBM_nombre )
        ie = gum.LazyPropagation( RB )
        
        #Agregar la evidencia historica de evaluaciones a la RB
        for nodo in RB.nodes():
            nombreNodo = RB.variable(nodo).name()
            gdc = self.NODOS[nombreNodo].grado_de_conocimiento
            
            if self.NODOS[nombreNodo].orden_evaluacion != -1:
                #print(" Tema " + str(nombreNodo) + " gdc: " + str(gdc) )
                ie.setEvidence({ str(nombreNodo) : int(gdc)})
          
        ie.makeInference()
        
        for nodo in RB.nodes():
            nombreNodo = RB.variable(nodo).name()
            self.NODOS[nombreNodo].matriz_inferencia[0] = ie.posterior(nombreNodo)[0] * 100
            self.NODOS[nombreNodo].matriz_inferencia[1] = ie.posterior(nombreNodo)[1] * 100
            self.NODOS[nombreNodo].matriz_inferencia[2] = ie.posterior(nombreNodo)[2] * 100

        # Promediar inferencias
        for nodo in self.SRB.nodes():
            nombre_nodo = self.SRB.variable(nodo).name()
            self.NODOS[nombre_nodo].matriz_inferencia_final[0] = (self.NODOS[nombre_nodo].matriz_inferencia[0] +
                                                                  self.NODOS[nombre_nodo].matriz_ponderacion[0]) / 2
            self.NODOS[nombre_nodo].matriz_inferencia_final[1] = (self.NODOS[nombre_nodo].matriz_inferencia[1] +
                                                                  self.NODOS[nombre_nodo].matriz_ponderacion[1]) / 2
            self.NODOS[nombre_nodo].matriz_inferencia_final[2] = (self.NODOS[nombre_nodo].matriz_inferencia[2] +
                                                              self.NODOS[nombre_nodo].matriz_ponderacion[2]) / 2

    def obtenerRBMA(self):
        return self.NODOS

    def obtenerItems(self):
        items = []
        i=0
        for nodo in self.NODOS:
            self.NODOS[nodo].discriminacion = 1  #
            if self.NODOS[nodo].matriz_inferencia[0] == 0 and self.NODOS[nodo].matriz_inferencia[1] == 0 and self.NODOS[nodo].matriz_inferencia[2] == 0:
                self.NODOS[nodo].adivinacion = self.NODOS[nodo].matriz_inferencia_final[0] / 100
            else:
                self.NODOS[nodo].adivinacion = self.NODOS[nodo].matriz_inferencia[0] / 100

            self.NODOS[nodo].asintota = 1  #
            
            #TO-DO: hacer dinamica la parte de comparar que no sea el area disciplinar o una de las ramas
            if not (self.NODOS[nodo].id == "1" or self.NODOS[nodo].id == "2" or self.NODOS[nodo].id == "14" or self.NODOS[
                nodo].id == "20" or self.NODOS[nodo].id == "13" or self.NODOS[nodo].id == "17" or self.NODOS[nodo].id == "40" or self.NODOS[
                        nodo].id == "51" or self.NODOS[nodo].id == "52"):
                item = [self.NODOS[nodo].discriminacion, self.NODOS[nodo].dificultad, self.NODOS[nodo].adivinacion,
                        self.NODOS[nodo].asintota, 0.0]
                
                i=i+1
            
                items.append(item)
        
        itemDificultadMayor = items[0][1]
        itemDificultadMenor = items[0][1]
        itemAdivinacionMayor = items[0][2]
        itemAdivinacionMenor = items[0][2] 
        
        for item in items:
            if item[2] < itemAdivinacionMenor:
                itemAdivinacionMenor = item[2]
          
            if item[2] > itemAdivinacionMayor:
                itemAdivinacionMayor = item[2]
                
            if item[1] < itemDificultadMenor:
                itemDificultadMenor = item[1]
            
            if item[1] > itemDificultadMayor:
                itemDificultadMayor = item[1]
        

        itemsNomralizados = []
        
        for item in items:
            itemNormal = []
            itemNormal.append( item[0] ) 
            itemNormal.append( (4--4)*(( item[1] - itemDificultadMenor )/( itemDificultadMayor - itemDificultadMenor ))+(-4) ) #Dificultad
            itemNormal.append( (0.2)*(( item[2] - itemAdivinacionMenor )/( itemAdivinacionMayor - itemAdivinacionMenor )) ) #Adivinación
            itemNormal.append( item[3] )
            itemsNomralizados.append( itemNormal ) 

        items = numpy.array(itemsNomralizados)
        return items
      
  
  