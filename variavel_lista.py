minha_lista = [1,2,3,4,5,"rocketseat",True,False]
#exibir lista inteira
print("Minha lista:",minha_lista)
#exibir posição especifica
print("Minha lista[0]:",minha_lista[0])
#exibir partes especificas - fatiamento - slice
print("Minha lista[1:7]:",minha_lista[1:7])
print("Minha lista[:6]:",minha_lista[:6])
print("Minha lista[3:]:",minha_lista[3:])

#metodos de lista

# append
minha_lista.append(666)
print("Minha lista:",minha_lista)
# index
indice = minha_lista.index(666)
print("indice do elemento 666:",indice)
# insert
minha_lista.insert(2, 10)
print("lista após insert",minha_lista)
# pop
elemento_removido = minha_lista.pop(3)
print("elemento removido",elemento_removido)
print("lista após pop(3)",minha_lista)
# remove
minha_lista[0] = "python"
minha_lista.remove(True)
print("lista após remove(true)",minha_lista)
# sort - ordenar
new_list = [1,2,4,55,88,5,3,9,10,9,5]
new_list.sort()
print("nova lista após sort",new_list)
