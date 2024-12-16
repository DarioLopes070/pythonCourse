idade = 20
if(idade >=60):
    print("Idoso")
elif(idade >=18):
    print("Maior de idade")
else:
    print("Menor de idade")

mensagem = "Você pode tirar carteira de habilitação" if idade >= 18 else "Você não pode tirar carteira de habilitação"
print(mensagem)