# usando IN
lista = [1,2,3,4,5,6]
for elemento in lista:
    print(elemento)

tupla = [1,2,3,4,5,6]
for elemento in tupla:
    print(elemento)

dicionario = {"nome": "Dário", "idade":23, "cidade":"Feira de Santana"}
for chave in dicionario.keys():
    print(chave)
for valor in dicionario.values():
    print(valor)
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")    

# usando RANGE
print(list(range(0,10)))
for numero in range (5):
    print("Numero:", numero)   
lista2 = [0,1,2,3,4,5]  
for indice in range(0, len(lista)):
    print("Indice", indice)
    print("elemento", lista2[indice])


# enumerate
lista_enumerate=["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")


# WHILE
contador = 0

while(contador<5):
    print(contador)
    contador+=1