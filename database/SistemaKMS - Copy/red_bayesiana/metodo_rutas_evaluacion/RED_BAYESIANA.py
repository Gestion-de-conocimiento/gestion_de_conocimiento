import pyAgrum as gum
import requests
from NODO import NODO

#En bash <python MPCN.py 'id_nodo' 'ponderación' 'saltos'>
class RED_BAYESIANA:
    def __init__(self, nombre_rbm):
        self.nodoEvidencia = ""
        self.ponderacionEvidencia = 0
        self.saltos = 0
        self.rangoDeAprovechamiento = 0
        self.subRedBayesiana = ""
        self.redBayesiana = gum.loadBN(nombre_rbm)
        self.caminos = ""

    def configurarParametros(self,parametros):
        self.nodoEvidencia = parametros[0]
        self.ponderacionEvidencia = int(parametros[1])
        self.saltos = int(parametros[2])
        self.caminos = parametros[3]
        if self.ponderacionEvidencia > 0 and self.ponderacionEvidencia <= 66:
            self.rangoDeAprovechamiento = 0
        elif self.ponderacionEvidencia > 66 and self.ponderacionEvidencia <= 83:
            self.rangoDeAprovechamiento = 1
        else:
            self.rangoDeAprovechamiento = 2

    def crearConexionesEnSubred(self, caminos, nodoCentral, esHaciaArriba):
        conexionesEnString = []
        for camino in caminos:
            if esHaciaArriba == True:
                camino.append(str(nodoCentral))
            else:
                camino.insert(0, str(nodoCentral))

            for i in range(len(camino)-1):
                conexionEnString = str(camino[i]) + "->" + str(camino[i+1])
                yaExisteConexion = False
                for conexion in conexionesEnString:
                    if(conexionEnString == conexion):
                        yaExisteConexion = True
                        break
                conexionesEnString.append(conexionEnString)
                if(yaExisteConexion==False):
                    self.subRedBayesiana.addArc( str(camino[i]), str(camino[i+1]) )

    def definirSubRedBayesiana(self):
        nodosDeLaSubRed = []
        adelante=[]
        atras=[]
        self.subRedBayesiana = gum.BayesNet('subred')
        self.subRedBayesiana.add(gum.LabelizedVariable(str(self.nodoEvidencia),str(self.nodoEvidencia),3))
        #URL = "http://104.248.232.150/arbol/caminoslibreria"
        #respuestaServidor = requests.get(url = URL)
        #data = respuestaServidor.json()
        #caminos = data['caminos']

        for a in self.caminos:
            for i in range(len(a)):
                if a[i] == int(self.nodoEvidencia):
                    if len(a)-1-i >=self.saltos:
                        adelante.append(a[i+1:i+ (self.saltos+1) ])
                    else:
                        adelante.append(a[i+1:i+len(a)-i])
                    if i >=3:
                        atras.append(a[i-self.saltos:i])
                    else:
                        atras.append(a[0:i])

        caminosAbajo = self.eliminarRepetidos(adelante)
        caminosArriba = self.eliminarRepetidos(atras)
        
        for camino in caminosAbajo: nodosDeLaSubRed += camino
        for camino in caminosArriba: nodosDeLaSubRed += camino

        nodosDeLaSubRed = self.eliminarRepetidos(nodosDeLaSubRed)

        for nodo in nodosDeLaSubRed:
            self.subRedBayesiana.add(gum.LabelizedVariable(str(nodo),str(nodo),3)) # ID, NOMBRE, ESTADOS

        self.crearConexionesEnSubred(caminosAbajo, self.nodoEvidencia, False)
        self.crearConexionesEnSubred(caminosArriba, self.nodoEvidencia, True)

    def cargarCPTSSubRedBayesiana(self):
        copiaRedBayesiana = self.redBayesiana

        nodosSubRed = self.subRedBayesiana.nodes()
        for nodo in nodosSubRed:
            nombreNodo = str( self.subRedBayesiana.variable(nodo).name() )
            
            padresSubRedBayesiana = self.subRedBayesiana.parents(self.subRedBayesiana.idFromName(nombreNodo))
            padresRedBayesianaMaestra = self.redBayesiana.parents(nombreNodo)

            for padreRBM in padresRedBayesianaMaestra:
                coincidecia = False
                nodoPadreRedBayesiana = self.redBayesiana.variable(padreRBM).name()
                for padre in padresSubRedBayesiana:
                    nodoPadreSubRedBayesiana = self.subRedBayesiana.variable(padre).name()
                    if nodoPadreRedBayesiana == nodoPadreSubRedBayesiana:
                        coincidecia = True
                        break
            
                if not coincidecia:
                    copiaRedBayesiana.eraseArc(copiaRedBayesiana.idFromName(nodoPadreRedBayesiana), copiaRedBayesiana.idFromName(nombreNodo))
            
            self.subRedBayesiana.cpt(nombreNodo).fillWith(copiaRedBayesiana.cpt(nombreNodo))

    def obtenerSubRed(self):
        self.definirSubRedBayesiana()
        self.cargarCPTSSubRedBayesiana()
        return self.subRedBayesiana

    def obtenerRedCompleta(self):
        return self.redBayesiana

    def eliminarRepetidos(self,m):
        if len(m) > 0:
            sr = []
            sr.append(m[0])
            for i in range(1, len(m)):
                v=0
                for a in sr:
                    if m[i]== a:
                        v=1
                if v==0:
                    sr.append(m[i])
            return sr

    def obtenerCaminosSubRed(self):
        caminos_ordenados = {}
        adelante = []
        atras = []
        for a in self.caminos:
            for i in range(len(a)):
                if str(a[i]) == self.nodoEvidencia:
                    if len(a) - 1 - i >= self.saltos:
                        adelante.append(a[i + 1:i + self.saltos + 1])
                    else:
                        adelante.append(a[i + 1:i + len(a) - i])
                    if i >= self.saltos:
                        atras.append(a[i - self.saltos:i])
                    else:
                        atras.append(a[0:i]) 
    
        eadelante = []
        if len(adelante) > 0:
            eadelante = self.eliminarRepetidos(adelante)
        eatras = []
        if len(adelante) > 0:
            eatras = self.eliminarRepetidos(atras)

        for i in range(len(eadelante)):
            for j in range(len(eadelante)):
                if len(eadelante[i]) < len(eadelante[j]):
                    eadelante2 = eadelante[i]
                    eadelante[i] = eadelante[j]
                    eadelante[j] = eadelante2

        for i in range(len(eatras)):
            for j in range(len(eatras)):
                if len(eatras[i]) < len(eatras[j]):
                    eatras2 = eatras[i]
                    eatras[i] = eatras[j]
                    eatras[j] = eatras2

        for i in range(len(eatras)):
            eatras[i] = eatras[i][::-1]

        caminos_ordenados['arriba'] = eatras
        caminos_ordenados['abajo'] = eadelante
        
        return caminos_ordenados

    '''def eliminarRepetidos(self, arreglo):
        sin_repetidos = []
        sin_repetidos.append(arreglo[0])
        for i in range(1, len(arreglo)):
            v = 0
            for a in sin_repetidos:
                if arreglo[i] == a:
                    v = 1
            if v == 0:
                sin_repetidos.append(arreglo[i])
        return sin_repetidos'''