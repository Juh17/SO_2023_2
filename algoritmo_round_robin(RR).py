import time

tarefas = [
    {"ingresso": 4, "duracao": 40, "prioridade": 4},
    {"ingresso": 1, "duracao": 20, "prioridade": 2},
    {"ingresso": 3, "duracao": 50, "prioridade": 1},
    {"ingresso": 0, "duracao": 30, "prioridade": 3}
]

quantum = 20
troca_contexto = 5

tempo_atual = 0
tempos_espera = []
tempos_vida = []
tempos_execucao = []
tempos_ingresso = []

while tarefas:
    tarefa_atual = tarefas.pop(0)
    
    inicio_execucao = max(tarefa_atual["ingresso"], tempo_atual)
    duracao_execucao = min(tarefa_atual["duracao"], quantum)
    
    tempos_ingresso.append((tarefa_atual["ingresso"], inicio_execucao))
    tempos_execucao.append((inicio_execucao, duracao_execucao))
    
    tempos_espera.append(inicio_execucao - tarefa_atual["ingresso"])
    tempos_vida.append(inicio_execucao - tarefa_atual["ingresso"] + duracao_execucao + troca_contexto + 10)
    
    tarefa_atual["duracao"] -= duracao_execucao
    tempo_atual = inicio_execucao + duracao_execucao + troca_contexto
    
    if tarefa_atual["duracao"] > 0:
        tarefas.append(tarefa_atual)

tempo_medio_espera = sum(tempos_espera) / len(tempos_espera)
tempo_medio_vida = sum(tempos_vida) / len(tempos_vida)


print(f'Tempo médio de espera: {tempo_medio_espera}')
print("Tempo médio de vida:", round(tempo_medio_vida, 2))
