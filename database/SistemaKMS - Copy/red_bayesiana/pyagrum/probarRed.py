import pyAgrum as gum
import numpy as np
bn=gum.loadBN("redbayesiana_servidor_localhost.bifxml")
ie=gum.LazyPropagation(bn)
print(ie.posterior("Conjuntos Numericos"))
ie.setEvidence({'Clasificación de los números': 0})
ie.makeInference()
A=ie.posterior("Conjuntos Numericos")
print(A)

e1=np.where(A[::]==max(A[::]))[0][0]
print(e1)
ie.makeInference()
A=ie.posterior("Conjuntos")
print(A)
ie.setEvidence({'Conjuntos Numericos': np.int32(e1).item()})
ie.makeInference()
A=ie.posterior("Conjuntos")
print(A)
e1=np.where(A[::]==max(A[::]))[0][0]
print(e1)

ie.makeInference()
A=ie.posterior("Aritmetica")
print(A)
ie.setEvidence({'Conjuntos': np.int32(e1).item()})
ie.makeInference()
A=ie.posterior("Aritmetica")
print(A)
e1=np.where(A[::]==max(A[::]))[0][0]
print(e1)
exit()
for i in range(len(A)):
 print(ie.posterior(A[i][0].strip()))  
exit()


print(ie.posterior("Ley de exponentes"))
ie.setEvidence({'Suma de números racionales':0, 'Multiplicación de números racionales': 1})
ie.makeInference()
print(ie.posterior("Ley de exponentes"))
ie.setEvidence({'Suma de números racionales':0, 'Multiplicación de números racionales': 1})
ie.makeInference()
print(ie.evidenceImpact("Ley de exponentes",["Conjuntos","Tablas de multiplicar"]))

