import pyAgrum as gum
import requests

#En bash <python MPCN.py 'id_nodo' 'ponderación' 'saltos'>
class SUB_RED_BAYESIANA:
    def __init__(self, parametros):
        self.nodoEvidencia = parametros[1]
        self.ponderacionEvidencia = int(parametros[2])
        self.saltos = int(parametros[3])
        self.rangoDeAprovechamiento = 0
        self.redBayesiana = ""
        self.subRedBayesiana = ""

        if self.ponderacionEvidencia > 0 and self.ponderacionEvidencia <= 66:
            self.rangoDeAprovechamiento = 0
        elif self.ponderacionEvidencia > 66 and self.ponderacionEvidencia <= 83:
            self.rangoDeAprovechamiento = 1
        else:
            self.rangoDeAprovechamiento = 2

        self.cargarRedBayesiana("../Redes/bn_ids_tres_estados_cuatro_expertos.bifxml")
        self.definirSubRedBayesiana()
        self.cargarCPTSSubRedBayesiana()

    def cargarRedBayesiana(self, ruta):
        self.redBayesiana=gum.loadBN(ruta)
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
        URL = "http://104.248.232.150/arbol/caminoslibreria"
        respuestaServidor = requests.get(url = URL)
        data = respuestaServidor.json()
        caminos = data['caminos']

        for a in caminos:
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
            nombreNodo = str(self.subRedBayesiana.variable(nodo).name())
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
        return self.subRedBayesiana

    '''def calcularInferenciaSubRed(self):
        ie=gum.LazyPropagation(self.subRedBayesiana)
        #ie.addEvidence('nodo', <valor>)
        #ie.makeInference()
        #gnb.showProba(ie.posterior("73"))
        
        #gnb.showInference(self.subRedBayesiana,evs={str(self.nodoEvidencia): self.rangoDeAprovechamiento},size=60)
        gnb.showBN(self.subRedBayesiana,size=60)
        
        nodosSubRed = self.subRedBayesiana.nodes()
        for nodo in nodosSubRed:
            nombreNodo = str(self.subRedBayesiana.variable(nodo).name())
            print(self.subRedBayesiana.cpt(nombreNodo)) '''


