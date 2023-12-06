def main():
    vetor_recursos_existentes = [5,4,2,1]
    vetor_recursos_disponiveis = [2,1,0,0]

    matriz_alocacao_corrente = [
        [0,0,1,0],
        [2,0,0,1],
        [0,1,2,0]
    ]

    matriz_de_requisicoes = [
        [2,0,0,1],
        [1,0,1,0],
        [2,1,0,1]
    ]

    linha_recursos_p1 = matriz_alocacao_corrente[0]
    linha_recursos_p2 = matriz_alocacao_corrente[1]
    linha_recursos_p3 = matriz_alocacao_corrente[2]

    linha_recursos_necessarios_p1 = matriz_de_requisicoes[0]
    linha_recursos_necessarios_p2 = matriz_de_requisicoes[1]
    linha_recursos_necessarios_p3 = matriz_de_requisicoes[2]
    recursos = usar_e_liberar_recursos(vetor_recursos_disponiveis, linha_recursos_necessarios_p1, linha_recursos_necessarios_p2, linha_recursos_necessarios_p3)
    verificar_impasse = verificar_igualdade_recursos(vetor_recursos_disponiveis, vetor_recursos_existentes)


    print(f'Vetor de recursos existentes: {vetor_recursos_existentes}')
    print(f'Vetor de recursos disponíveis: {vetor_recursos_disponiveis}')
    print(f'\nMatriz de alocação corrente: {matriz_alocacao_corrente}')
    print(f'\nMatriz de requisições: {matriz_de_requisicoes}')

    
    print(verificar_impasse)

def usar_e_liberar_recursos(disponiveis, requeridos_p1, requeridos_p2, requeridos_p3):
    
    for i in range(len(disponiveis)):
        if all(requeridos_p1) <= disponiveis[i]:
            disponiveis[i] += requeridos_p1[i]     
        if all(requeridos_p2) <= disponiveis[i]:
            disponiveis[i] += requeridos_p2[i]
            #print(vetor_recursos_disponiveis)     
        if all(requeridos_p3) <= disponiveis[i]:
            disponiveis[i] += requeridos_p3[i]
        break
    print('Há algum processo em deadlock/impasse')

    return disponiveis
  


def verificar_igualdade_recursos(disponiveis, existentes):
 
    for recurso in range(len(disponiveis)):
        if disponiveis[recurso] == existentes[recurso]:
            return 'Todos os processos rodaram'
        else:
            return 'Pode haver impasse/deadlock'
        

main()
