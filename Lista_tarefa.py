def adicionar_tarefa(lista):
    tarefa = input('Descreva a tarefa: ')
    lista.append(tarefa)
    print('Tarefa adicionada com sucesso!')

def remover_tarefa(lista):
    if len(lista) == 0:
        print('Não tem tarefas!')
    else:
        print(lista)
        tarefa_removida = input('Informe a tarefa que deseja remover: ')
        if tarefa_removida in lista:
            lista.remove(tarefa_removida)
            print(f"A tarefa '{tarefa_removida}' foi removida com sucesso!")
        else:
            print('Tarefa não encontrada!')
        print(lista)

def exibir_tarefas(lista):
    if len(lista) == 0:
        print('Não tem tarefas pendentes.')
    else:
        print('Tarefas pendentes:')
        for i, tarefa in enumerate(lista):
            print(f"{i+1}. {tarefa}")
        print()

def marcar_concluida(lista):
    if len(lista) == 0:
        print('Não tem tarefas!')
    else:
        print(lista)
        tarefa_concluida = input('Informe a tarefa que deseja marcar como concluída: ')
        if tarefa_concluida in lista:
            lista.remove(tarefa_concluida)
            print(f"A tarefa '{tarefa_concluida}' foi marcada como concluída!")
        else:
            print('Tarefa não encontrada!')
        print(lista)

def main():
    lista = []
    while True:
        print('======= MENU =======')
        print('1. Adicionar tarefa')
        print('2. Remover tarefa')
        print('3. Exibir tarefas pendentes')
        print('4. Marcar tarefa como concluída')
        print('5. Sair')
        opcao = int(input('Informe a opção: '))

        if opcao == 1:
            adicionar_tarefa(lista)
        elif opcao == 2:
            remover_tarefa(lista)
        elif opcao == 3:
            exibir_tarefas(lista)
        elif opcao == 4:
            marcar_concluida(lista)
        elif opcao == 5:
            print('Aplicativo encerrado.')
            break
        else:
            print('Opção inválida')

if __name__ == '__main__':
    main()