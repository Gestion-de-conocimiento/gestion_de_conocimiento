#from  ~/SistemaKMS import cargarTemas


import sys
# insert at position 1 in the path, as 0 is the path of this file.
sys.path.insert(1, '~/SistemaKMS')

import cargarTemas

file.function()
temas= cargarTemas.temas()
padres=temas[0]
for i in range(len(padres)):
  print(padres[i])
for i in range(len(padres)):
  print(padres[i])