def painel():
    while True:
        print("""Gerenciador de Tarefas

1 - Adicionar Tarefa
2 - Gerenciar Tarefas
3 - Estatísticas
4 - Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "4":
            print("Saindo...")
            break
        else:
            print(f"Você escolheu a opção {opcao}")


painel()
