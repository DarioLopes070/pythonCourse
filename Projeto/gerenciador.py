def adicionar_tarefa(tarefas, nome_tarefa):
    tarefas.append({"tarefa": nome_tarefa, "completada": False})
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return 
def ver_tarefas(tarefas):
    # item = list(tarefas.items())
    print("\nLista de tarefas:")
    # for x in range (len(tarefas)):
    #     print(str(x+1)+" - "+tarefas[x]["tarefa"])
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return
def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    if((indice_tarefa-1)>=0 and (indice_tarefa-1)<=len(tarefas)):
        tarefas[indice_tarefa-1]["tarefa"]=novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Índice de tarefa inválido")
    return
def concluir_tarefa(tarefas, indice_tarefa):
    if((indice_tarefa-1)>=0 and (indice_tarefa-1)<=len(tarefas)):
        tarefas[indice_tarefa-1]["completada"]=True
        print(f"Tarefa {indice_tarefa} completada com sucesso!")
    else:
        print("Índice de tarefa inválido")
    return
def deletar_tarefa_concluida(tarefas):
    # for indice, tarefa in enumerate(tarefas):
    #     if tarefa["completada"]:
    #         del tarefas[indice]
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas concluidas foram deletadas com sucesso!")
    return
tarefas = []
while True:
    print("\nMenu do gerenciador de lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")
    resposta = int(input("Digite a opção escolhida:"))
    match resposta:
        case 1:
            nome_tarefa = input("Digite o nome da tarefa que deseja adicinar: ")
            adicionar_tarefa(tarefas, nome_tarefa)
        case 2:
            ver_tarefas(tarefas)    
        case 3:
            ver_tarefas(tarefas)    
            indice_tarefa = int(input("Digite o numero da tarefa que deseja atualizar: "))
            novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
            atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
        case 4:
            ver_tarefas(tarefas)    
            indice_tarefa = int(input("Digite o numero da tarefa que deseja concluir: "))
            concluir_tarefa(tarefas, indice_tarefa)
        case 5:
            deletar_tarefa_concluida(tarefas)
            ver_tarefas(tarefas)    
        case 6:
            break
        case _:
            print("Entrada inválida")
            # break
    # if(resposta == 6):
    #     break
print("programa finalizado")   