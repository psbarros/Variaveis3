# Não se esqueça de incluir o módulo numpy
# Use o navegador Chrome, para copiar/colar a entrada de exemplo 
from numpy import *

vetor = array(eval(input("vetor: ")))
v1 = sum(vetor) / size(vetor)
print(size(vetor))
print(vetor[0])
print(vetor[-1])
print(max(vetor))
print(min(vetor))
print(sum(vetor))
print(round(v1, 2))