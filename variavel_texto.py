nome_completo = "Dário Lopes"
nome_completo_aspas = """Dário 
Lopes"""
nome_completo_quebra = "Dário \
Lopes"
nome = "Dário"
sobrenome = "Lopes"
#formatação e modo de  imprimir

print("nome completo(1ª forma):", nome_completo)
print("nome completo(2ª forma):" + nome_completo)
print("nome completo(3ª forma):" + "Dário" + "Lopes")
print("nome completo(4ª forma):" + "Dário", "Lopes")
print("nome completo(5ª forma):", nome_completo_aspas)
print("nome completo(6ª forma):", nome_completo_quebra)
print("nome completo(7ª forma): %s" % nome_completo_quebra)
print("nome completo(8ª forma): %s %s" % (nome, sobrenome))
print(f"nome completo(9ª forma): {nome} {sobrenome}")
print("nome completo(10ª forma): {} {}".format(nome, sobrenome))

#metodos

# count
print(nome_completo.count("a"))
# find
print(nome_completo.find("a"))
# encode -> transforma em bits
print(nome_completo.encode())
# decode -> transforma bits em string
print(nome_completo.encode().decode())
# replace
print(nome_completo.replace("a", "123"))
# join
print("-".join(nome_completo))
# split
print(nome_completo.split())
# strip
novo_nome = "xDario LopesX"
print(nome_completo.strip("x"))
print(nome_completo.rstrip("x")) #right strip
print(nome_completo.lstrip("x")) #left strip
#startswith
print(nome_completo.startswith("D"))
#in
print("es" in nome_completo)
#not in
print("abc" not in nome_completo)

