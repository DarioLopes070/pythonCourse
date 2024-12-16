pessoa = {"nome": "Dário", "idade":23, "cidade":"Feira de Santana"}
print("Meu dicionario de exemplo:",pessoa)
print("Nome:",pessoa["nome"])
print("Idade:",pessoa["idade"])
print("Cidade:",pessoa["cidade"])
pessoa["sobrenome"] = "Lopes"
print("Sobrenome:",pessoa["sobrenome"])
pessoa["idade"] = 25
print("Idade atualizada:",pessoa["idade"])

#remover chave/valor

del pessoa["sobrenome"]
print("Meu dicionario de exemplo:",pessoa)

# métodos

#keys
chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

#values
valor = list(pessoa.values())
print("valores do dicionário:", valor)
print("Primeiro valor do dicionario:", valor[0])

#items -> gera tuplas com valores de chave e valor juntos
item = list(pessoa.items())
print("pares chaves-valor do dicionário:", item)
print("Primeira chave/valor do dicionario:", item[0])
print("Primeira chave/valor do dicionario: %s = %s" % (item[0][0], item[0][1]))
