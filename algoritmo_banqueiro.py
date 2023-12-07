def pode_executar(disponiveis, alocados, requisicoes, processo):
    for i in range(4):
        if requisicoes[processo][i] > disponiveis[i]:
            return False
    return True

def executar(disponiveis, alocados, requisicoes, processo):
    for i in range(4):
        disponiveis[i] += alocados[processo][i]
        alocados[processo][i] = 0

def main():
    recursos_existentes = [4, 2, 3, 1]
    recursos_disponiveis = [2, 1, 0, 0]

    matriz_alocacao_concorrente = [
        [0, 0, 1, 0],
        [2, 0, 0, 1],
        [0, 1, 2, 0]
    ]

    matriz_requisicoes = [
        [2, 0, 0, 1],
        [1, 0, 1, 0],
        [2, 1, 0, 0]
    ]

    foi_executado = [False] * 3

    print("Recursos existentes:", recursos_existentes)
    print("Recursos disponíveis:", recursos_disponiveis)

    print("Matriz de alocação concorrente:")
    nomes_processos = ["p1", "p2", "p3"]
    for i in range(3):
        print(nomes_processos[i], matriz_alocacao_concorrente[i])

    print("Matriz de requisições:")
    for i in range(3):
        print(nomes_processos[i], matriz_requisicoes[i])

    while True:
        executou = False

        for i in range(3):
            if not foi_executado[i] and pode_executar(recursos_disponiveis, matriz_alocacao_concorrente, matriz_requisicoes, i):
                executar(recursos_disponiveis, matriz_alocacao_concorrente, matriz_requisicoes, i)
                print(f"Processo {nomes_processos[i]} executado.")
                print("Recursos disponíveis:", recursos_disponiveis)
                foi_executado[i] = True
                executou = True

        if not executou:
            break

        todos_executados = all(foi_executado)
        if todos_executados:
            break

    nao_executado = any(not e for e in foi_executado)
    if nao_executado:
        print("Há deadlock.")
    else:
        print("Não há deadlock.")

main()
