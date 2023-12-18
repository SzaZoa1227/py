f = open('be.txt','rt')
lista = []
for sor in f:
    print(sor,end="")
    lista.append(sor.rstrip())  
print(lista) 