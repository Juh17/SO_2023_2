import os
from functions_banqueiro import *


vetor_recursos_existentes = [4,3,2,1]
vetor_recursos_disponiveis = [2,1,0,0]

matriz_alocacao_corrente = [
    [0,0,1,0],
    [2,0,0,1],
    [0,1,2,0]
]

matriz_de_requisicoes = [
    [0,0,1,0],
    [2,0,0,1],
    [0,1,2,0]
]

def main():
    print(16 * '#' + '-Algoritmo do Banqueiro-' + 16 * '#')
    qtd_processos = int(input('Quantos processos estão em execução? '))

    qtd_tipos_recursos = int(input('Quantos tipos de recursos cada processo vai necessitar? '))

    recursos_totais = get_recursos_totais(qtd_tipos_recursos)

    matriz_alocados = get_matriz_alocados(qtd_processos, qtd_tipos_recursos)

    recursos_alocados = get_vetor_recursos_alocados(matriz_alocados)

    recursos_disponiveis = get_vetor_recursos_disponiveis(recursos_totais, recursos_alocados)

    matriz_recursos_necessarios = get_matriz_recursos_necessarios(qtd_processos, qtd_tipos_recursos)

    input('Pressione Enter para continuar.....')

    os.system('clear')

    imprimir_os_dados(recursos_totais, matriz_alocados, recursos_alocados, recursos_disponiveis, matriz_recursos_necessarios)

    algoritmo_banqueiro(qtd_processos, qtd_tipos_recursos, recursos_disponiveis, matriz_recursos_necessarios, matriz_alocados)


if __name__ == '__main__':
    main()