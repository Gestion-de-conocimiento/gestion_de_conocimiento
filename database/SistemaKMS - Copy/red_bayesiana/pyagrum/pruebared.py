import pyAgrum as gum
import pyAgrum.causal as csl
import os

mtt = gum.fastBN("court order->captain->soldier A->death<-soldier B<-captain")
# filling the CPTs
def smallPertubation(cpt,epsilon=0.0001):
    cpt.fillWith(cpt.translate(epsilon).normalizeAsCPT())
    
mtt.cpt("court order")[:] = [0.5, 0.5]

# The captain will give the signal only if the court gives the order.
mtt.cpt("captain")[{"court order":0}] = [1,0] 
mtt.cpt("captain")[{"court order":1}] = [0,1] 

# The soldiers only fire if the captain gives them the signal.
mtt.cpt("soldier A")[{"captain":0}] = [1, 0] # c=0
mtt.cpt("soldier A")[{"captain":1}] = [0, 1] # c=1
smallPertubation(mtt.cpt("soldier A"))

mtt.cpt("soldier B")[{"captain":0}] = [1, 0] # c=0
mtt.cpt("soldier B")[{"captain":1}] = [0, 1] # c=1
smallPertubation(mtt.cpt("soldier B"))

# It only takes one of the two soldiers to shoot for the prisoner to die.
mtt.cpt("death")[{"soldier A":0,"soldier B":0}] = [1, 0] # a=0,b=0
mtt.cpt("death")[{"soldier A":0,"soldier B":1}] = [0, 1] # a=0,b=1
mtt.cpt("death")[{"soldier A":1,"soldier B":0}] = [0, 1] # a=1,b=0
mtt.cpt("death")[{"soldier A":1,"soldier B":1}] = [0, 1] # a=1,b=1
smallPertubation(mtt.cpt("death"))
 
# inference engine : LazyPropagation
ie = gum.LazyPropagation(mtt)

ie.makeInference()
print(ie.posterior("death"))
# Knowing that death = 1
ie.makeInference()
print(ie.posterior("court order"))
ie.setEvidence({'death':1})
ie.makeInference()
print(ie.posterior("court order"))