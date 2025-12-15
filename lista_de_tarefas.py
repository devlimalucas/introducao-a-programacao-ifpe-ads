tarefas = []
proximo_id = 1


def adicionar_tarefa():
    global proximo_id
    descricao = input("Descrição: ")
    print("Prioridade: 1-Alta | 2-Média | 3-Baixa")
    prio_opcao = input("Escolha: ")

    if prio_opcao == "1":
        prioridade = "Alta"
    elif prio_opcao == "2":
        prioridade = "Média"
    else:
        prioridade = "Baixa"

    prazo = input("Prazo (opcional, formato YYYY-MM-DD): ")
    tarefa = {
        "id": proximo_id,
        "descricao": descricao,
        "prioridade": prioridade,
        "prazo": prazo if prazo else "-",
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    proximo_id += 1
    print("Tarefa adicionada!\n")


def listar_tarefas(filtro=0, prioridade=0):
    print("\n=== Lista de Tarefas ===")
    for t in tarefas:
        if filtro == 1 and t["status"] != "Pendente":
            continue
        if filtro == 2 and t["status"] != "Concluída":
            continue
        if prioridade == 1 and t["prioridade"] != "Alta":
            continue
        if prioridade == 2 and t["prioridade"] != "Média":
            continue
        if prioridade == 3 and t["prioridade"] != "Baixa":
            continue

        print(
            f"[{t['id']}] {t['descricao']} | "
            f"{t['prioridade']} | {t['status']} | Prazo: {t['prazo']}"
        )
    print()


def concluir_tarefa():
    id_tarefa = int(input("ID da tarefa a concluir: "))
    for t in tarefas:
        if t["id"] == id_tarefa:
            t["status"] = "Concluída"
            print("Tarefa concluída!\n")
            return
    print("ID não encontrado.\n")


def editar_tarefa():
    id_tarefa = int(input("ID da tarefa a editar: "))
    for t in tarefas:
        if t["id"] == id_tarefa:
            nova_desc = input("Nova descrição (Enter para manter): ")
            print("Nova prioridade: 1-Alta | 2-Média" +
                  "| 3-Baixa | Enter para manter")
            nova_prio = input("Escolha: ")
            novo_prazo = input("Novo prazo (Enter para manter): ")

            if nova_desc:
                t["descricao"] = nova_desc
            if nova_prio == "1":
                t["prioridade"] = "Alta"
            elif nova_prio == "2":
                t["prioridade"] = "Média"
            elif nova_prio == "3":
                t["prioridade"] = "Baixa"
            if novo_prazo:
                t["prazo"] = novo_prazo

            print("Tarefa atualizada!\n")
            return
    print("ID não encontrado.\n")


def remover_tarefa(opcao_rem):
    global tarefas
    if (opcao_rem == 1):
        id_tarefa = int(input("ID da tarefa a remover: "))
        for t in tarefas:
            if t["id"] == id_tarefa:
                tarefas.remove(t)
                print("Tarefa removida!\n")
                return
    if (opcao_rem == 2):
        tarefas = []


def estatisticas():
    total = len(tarefas)
    concluidas = sum(1 for t in tarefas if t["status"] == "Concluída")
    pendentes = total - concluidas
    progresso = (concluidas / total * 100) if total > 0 else 0
    print("\n=== Estatísticas ===")
    print(f"Total: {total}")
    print(f"Pendentes: {pendentes}")
    print(f"Concluídas: {concluidas}")
    print(f"Progresso: {progresso:.1f}%\n")


def menu():
    while True:
        print("=== Gerenciador de Tarefas ===")
        print("1 - Adicionar tarefa")
        print("2 - Editar tarefa")
        print("3 - Remover tarefa")
        print("4 - Concluir tarefa")
        print("5 - Listar tarefas")
        print("6 - Listar por prioridade")
        print("7 - Estatísticas")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            editar_tarefa()
        elif opcao == "3":
            print("1 - Remover por ID | 2 - Remover Todas")
            opcao_rem = int(input("Escolha: "))
            remover_tarefa(opcao_rem)
        elif opcao == "4":
            concluir_tarefa()
        elif opcao == "5":
            print("1 - Todas | 2 - Pendentes | 3 - Concluídas")
            filtro = int(input("Escolha: "))
            listar_tarefas(filtro=filtro - 1)
        elif opcao == "6":
            print("1 - Alta | 2 - Média | 3 - Baixa")
            prio = int(input("Escolha: "))
            listar_tarefas(prioridade=prio)
        elif opcao == "7":
            estatisticas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")


menu()
