import requests

def temas():
  URL = "http://localhost/arbol/caminoslibreria"
  r = requests.get(url = URL)
  data = r.json()
  numeros = []
  letras = []
  padres = []
  nodos = data['nodos']
  caminos = data['caminos']
  temas = data['temas']
  numeros = []
  letras = []
  for i in range( len(nodos) ):
    for j in range( len(temas)):
      if(temas[j]['id'] == nodos[i]):
        letras.append(temas[j]['nombre'])
      numeros.append(i)
  padres_ids = []
  for i in range(len(nodos)): 
      padres_nodo = []
      padres_nodo_id = []
      padres_nodo.append(letras[i])
      padres_nodo_id.append(nodos[i])
      for j in range(len(caminos)):
          for k in range( len(caminos[j]) ):
            if(caminos[j][k] == nodos[i] and k > 0 ):
              repetido = 0
              for l in range( len(padres_nodo) ):
                if padres_nodo[l]  == letras[nodos.index(caminos[j][k-1])]:
                  repetido = 1
                  break
              if repetido == 0:
                padres_nodo.append( letras[nodos.index(caminos[j][k-1])] )
                padres_nodo_id.append( caminos[j][k-1] )
      padres.append(padres_nodo)
      padres_ids.append(padres_nodo_id) 
  return [padres,padres_ids]