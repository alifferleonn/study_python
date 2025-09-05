from funcoes_tarefas import (
    carregar_tarefas,
    adicionar_tarefa,
    listar_tarefas,
    marcar_tarefa_concluida,
    remover_tarefa
)

def main():
    tarefas = carregar_tarefas()
    print("======================================================")
    print("=============== Organizador de Tarefas: ==============")
    print("======================================================")

    while True:
        print("\nComandos: adicionar, listar, concluir, remover, sair")
        comando = input("Digite um comando: ").lower().split(maxsplit=1)

        acao = comando[0]
        argumento = comando[1] if len(comando) > 1 else None

        if acao == 'adicionar' and argumento:
            adicionar_tarefa(tarefas, argumento)
        elif acao == 'listar':
            listar_tarefas(tarefas)
        elif acao == 'concluir' and argumento:
            marcar_tarefa_concluida(tarefas, argumento)
        elif acao == 'remover' and argumento:
            remover_tarefa(tarefas, argumento)
        elif acao == 'sair':
            print("Saindo do gerenciador de tarefas. Até mais!")
            break
        else:
            print("Comando inválido ou argumento faltando. Tente novamente.")

if __name__ == "__main__":
    main()