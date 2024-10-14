import cargarTemas
temas= cargarTemas.temas()
indices=temas[0]
padres=temas[1]
padres_ids=temas[2]


for i in range(len(padres)):
  print(padres[i])