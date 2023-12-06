def main():
    vetor_recursos_existentes = [4,3,2,1]
    vetor_recursos_disponiveis = [2,1,0,0]

    matriz_alocacao_corrente = [
        [0,0,1,0],
        [2,0,0,1],
        [0,1,2,0]
    ]

    matriz_requisicoes = [
        [2,0,0,1],
        [1,0,1,0],
        [2,1,0,0]
    ]

    recursos_p1 = matriz_alocacao_corrente[0]
    recursos_p2 = matriz_alocacao_corrente[1]
    recursos_p3 = matriz_alocacao_corrente[2]

    recursos_necessarios_p1 = matriz_requisicoes[0]
    recursos_necessarios_p2 = matriz_requisicoes[1]
    recursos_necessarios_p3 = matriz_requisicoes[2]
    recursos = usar_e_liberar(vetor_recursos_disponiveis, recursos_necessarios_p1, recursos_necessarios_p2, recursos_necessarios_p3)
    verificar_impasse = igualdade_recursos(vetor_recursos_disponiveis, vetor_recursos_existentes)


    print(f'Recursos existentes: {vetor_recursos_existentes}')
    print(f'Recursos disponíveis: {vetor_recursos_disponiveis}')
    print(f'\nMatriz de alocação corrente: {matriz_alocacao_corrente}')
    print(f'\nMatriz de requisições: {matriz_requisicoes}')

    
    print(verificar_impasse)


def usar_e_liberar(disponiveis, p1, p2, p3):
    deadlock = True  
    alocou_recursos = False  

    for i in range(len(disponiveis)):
       
        if all(p1) <= disponiveis[i]:
            disponiveis[i] += p1[i]
            alocou_recursos = True  
            deadlock = False 
        if all(p2) <= disponiveis[i]:
            disponiveis[i] += p2[i]
            alocou_recursos = True 
            deadlock = False 
        if all(p3) <= disponiveis[i]:
            disponiveis[i] += p3[i]
            alocou_recursos = True  
            deadlock = False  

    # Verifica se nenhum processo alocou recursos
    if not alocou_recursos:
        print('Todos os processos estão em deadlock/impasse')

    return disponiveis

def igualdade_recursos(disponiveis, existentes):
    for recurso in range(len(disponiveis)):
        if disponiveis[recurso] != existentes[recurso]:
            return 'Pode haver impasse/deadlock'
    return 'Todos os processos rodaram'


main()
