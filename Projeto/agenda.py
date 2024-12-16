def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, favoritar_contato):
    contatos.append({"nome": nome_contato, "telefone": telefone_contato, "email":email_contato, "favorito": False}) if favoritar_contato=="2" else contatos.append({"nome": nome_contato, "telefone": telefone_contato, "email":email_contato, "favorito": True})
    print(f"O contato de {nome_contato} foi adicionado com sucesso!")
    return 
def ver_contatos(contatos):
    # item = list(contatos.items())
    print("\nLista de contatos:\n")
    # for x in range (len(contatos)):
    #     print(str(x+1)+" - "+contatos[x]["tarefa"])
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        print(f"{indice}. [{status}] {nome_contato} {telefone_contato}")
    return
def ver_contatos_favoritos(contatos):
    # item = list(contatos.items())
    print("\nLista de contatos favoritos:\n")
    # for x in range (len(contatos)):
    #     print(str(x+1)+" - "+contatos[x]["tarefa"])
    for indice, contato in enumerate(contatos, start=1):
        if(contato["favorito"]):
            status = "★" 
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            print(f"{indice}. [{status}] {nome_contato} {telefone_contato}")
    return
def atualizar_tarefa(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato, novo_favoritar_contato):
    if((indice_contato-1)>=0 and (indice_contato-1)<=len(contatos)):
        contatos[indice_contato-1]["nome"]=novo_nome_contato
        contatos[indice_contato-1]["telefone"]=novo_telefone_contato
        contatos[indice_contato-1]["email"]=novo_email_contato
        if(novo_favoritar_contato =="2"):
            contatos[indice_contato-1]["favorito"]=False 
        else :
            contatos[indice_contato-1]["favorito"]=True
        print(f"Contato {novo_nome_contato} atualizado para {novo_telefone_contato}")
    else:
        print("Índice de tarefa inválido")
    return
def marcar_desmarcar_contato_favorito(contatos, indice_contato):
    if((indice_contato-1)>=0 and (indice_contato-1)<=len(contatos)):
        if(contatos[indice_contato-1]["favorito"]):
            contatos[indice_contato-1]["favorito"]=False
            print(f"Contato {indice_contato} desfavoritado com sucesso!")
        else:    
            contatos[indice_contato-1]["favorito"]=True
            print(f"Contato {indice_contato} favoritado com sucesso!")
    else:
        print("Índice de tarefa inválido")
    return
def deletar_contato(contatos, indice_contato):
    if((indice_contato-1)>=0 and (indice_contato-1)<=len(contatos)):
        del contatos[indice_contato-1]
        print(f"Contato {indice_contato} deletado com sucesso!")
    else:
        print("Índice de contato inválido")
    return
contatos = []
while True:
    print("\nAgenda Telefônica:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Favoritar/desfavoritar contato")
    print("5. Ver favoritos")
    print("6. Deletar contato")
    print("7. Sair")
    resposta = int(input("Digite a opção escolhida:"))
    match resposta:
        case 1:
            nome_contato = input("Digite o nome do contato: ")
            telefone_contato = input("Digite o numero de telefone: ")
            email_contato = input("Digite o email do contato: ")
            favoritar_contato = input("Deseja favoritar o contato?\n1 - SIM\n2 - NÃO\n")
            adicionar_contato(contatos, nome_contato, telefone_contato, email_contato, favoritar_contato)
        case 2:
            ver_contatos(contatos)    
        case 3:
            ver_contatos(contatos)    
            indice_contato = int(input("Digite o numero do contato que deseja atualizar: "))
            novo_nome_contato = input("Digite o nome do contato: ")
            novo_telefone_contato = input("Digite o numero de telefone: ")
            novo_email_contato = input("Digite o email do contato: ")
            novo_favoritar_contato = input("Deseja favoritar o contato?\n1 - SIM\n2 - NÃO\n")            
            atualizar_tarefa(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato, novo_favoritar_contato)
        case 4:
            ver_contatos(contatos)    
            indice_contato = int(input("Digite a posição do numero que deseja favoritar: "))
            marcar_desmarcar_contato_favorito(contatos, indice_contato)
        case 5:
            ver_contatos_favoritos(contatos)    
        case 6:
            ver_contatos(contatos)    
            indice_contato = int(input("Digite a posição do numero que deseja deletar: "))
            deletar_contato(contatos, indice_contato)
            ver_contatos(contatos)    
        case 7:
            break
        case _:
            print("Entrada inválida")
            # break
    # if(resposta == 6):
    #     break
print("programa finalizado")   