import pyAgrum as gum
bn=gum.loadBN("rbm_1.bifxml")
ie=gum.LazyPropagation(bn)
ie.makeInference()

for nodo in bn.nodes():
  

print(ie.posterior(bn.idFromName("30")))