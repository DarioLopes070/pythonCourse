#diferente das listas é imutavel, não permite alteração dos elementos
minha_tupla = (1,2,3,2,4,5,2)

print("minha_tupla:",minha_tupla)

print("minha_tupla[0]:",minha_tupla[0])
print("minha_tupla[2]:",minha_tupla[2])
print("minha_tupla[-1]:",minha_tupla[-1]) #acessa ultimo elemento

# método
# count
contagem = minha_tupla.count(2)
print("quantidade de vezes que o numero 2 aparece:",contagem)
#index
indice = minha_tupla.index(3)
print("indice da primeira ocorrencia do numero 3:",indice)
