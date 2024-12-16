#exemplo de importação de módulo padrão
# import math

# num = int(input("Digite um numero para descobrir sua raiz quadrada: "))
# raiz = math.sqrt(num)
# print(f"resultado: {raiz}")

#exemplo 2 de importação de módulo padrão, pegando apenas função especifica
# from math import sqrt

# num = int(input("Digite um numero para descobrir sua raiz quadrada: "))
# raiz = sqrt(num)
# print(f"resultado: {raiz}")


#exemplo de importação de módulo personalisado
import meu_modulo

mensagem = meu_modulo.saudacao("Dario")
dobro = meu_modulo.dobro(35)

print(mensagem)
print(dobro)
