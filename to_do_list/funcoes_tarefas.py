import json
import os

ARQUIVO_TAREFAS = 'tarefas.json'

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def adicionar_tarefa(tarefas, titulo):
    nova_tarefa = {
        'id': len(tarefas) + 1,
        'titulo': titulo,
        'concluida': False
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f"Tarefa '{titulo}' adicionada.")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa listada.")
        return

    print("\n=== Minhas Tarefas ===")
    for tarefa in tarefas:
        status = "✓" if tarefa['concluida'] else "✗"
        print(f"[{status}] ID: {tarefa['id']} - {tarefa['titulo']}")
    print("======================")

def marcar_tarefa_concluida(tarefas, tarefa_id):
    try:
        tarefa_id = int(tarefa_id)
        for tarefa in tarefas:
            if tarefa['id'] == tarefa_id:
                tarefa['concluida'] = True
                salvar_tarefas(tarefas)
                print(f"Tarefa ID {tarefa_id} marcada como concluída.")
                return
        print(f"Erro: Tarefa com ID {tarefa_id} não encontrada.")
    except ValueError:
        print("Erro: O ID da tarefa deve ser um número inteiro.")

def remover_tarefa(tarefas, tarefa_id):
    try:
        tarefa_id = int(tarefa_id)
        tarefas_restantes = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]

        if len(tarefas_restantes) < len(tarefas):
            salvar_tarefas(tarefas_restantes)
            print(f"Tarefa ID {tarefa_id} removida com sucesso.")
        else:
            print(f"Erro: Tarefa com ID {tarefa_id} não encontrada.")
    except ValueError:
        print("Erro: O ID da tarefa deve ser um número inteiro.")