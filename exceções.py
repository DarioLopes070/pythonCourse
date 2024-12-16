# try:
#     numero = int(input("Digite um numero inteiro: "))
#     resultado = 10 / numero
#     print(f"resultado = {resultado}")
# except ValueError as e:
#     print(f"erro tipo value error: {e}")
#     raise ValueError("Tipo de variaveis incompativeis")
# except Exception as e:
#     print(f"erro: {e}")

try:
    numero = int(input("Digite um numero inteiro: "))
    resultado = 10 / numero
except ValueError as e:
    print(f"erro tipo value error: {e}")
    raise ValueError("Tipo de variaveis incompativeis")
except Exception as e:
    print(f"erro: {e}")
# executa o else somente se o try funcionar
else:
    print(f"resultado = {resultado}")
# executa o finally independente se o try funcionou ou não
finally:
    print("Operação finalizada!")
