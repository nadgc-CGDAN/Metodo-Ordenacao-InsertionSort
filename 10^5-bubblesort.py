import time
import random

def bubble_sort(array):
    """Ordena um array usando o algoritmo Bubble Sort."""
    n = len(array)
    comparacoes = 0  # Contador para comparações
    trocas = 0       # Contador para trocas
    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1  # Incrementa o contador de comparações
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                trocas += 1  # Incrementa o contador de trocas
        print(f"Iteração {i+1}: {array}")  # Mostra o array após cada iteração
    return array, comparacoes, trocas

def main():
    """Função principal que executa o programa."""
    array = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]  # Array de exemplo
    size = 10**5  # Tamanho do array aleatório

    # Gera um array aleatório de tamanho 10^4
    array_random = [random.randint(0, 100) for _ in range(size)]

    # Inicia a contagem de tempo para o array de exemplo
    start_time_example = time.time()

    # Ordena o array de exemplo em ordem decrescente usando o bubble sort e obtém contagem de comparações e trocas
    sorted_array_example, comparacoes_example, trocas_example = bubble_sort(array.copy())

    # Finaliza a contagem de tempo para o array de exemplo
    end_time_example = time.time()

    # Imprime o array de exemplo ordenado
    print("Array de exemplo ordenado:")
    print(sorted_array_example)

    # Imprime o número de comparações e trocas realizadas para o array de exemplo
    print("Número de comparações para o array de exemplo:", comparacoes_example)
    print("Número de trocas para o array de exemplo:", trocas_example)

    # Calcula e imprime o tempo de execução para o array de exemplo
    execution_time_example = end_time_example - start_time_example
    print(f"Tamanho do array de exemplo: {len(array)}, Tempo de execução: {execution_time_example} segundos")

    # Inicia a contagem de tempo para o array aleatório
    start_time_random = time.time()

    # Ordena o array aleatório em ordem decrescente usando o bubble sort e obtém contagem de comparações e trocas
    sorted_array_random, comparacoes_random, trocas_random = bubble_sort(array_random.copy())

    # Finaliza a contagem de tempo para o array aleatório
    end_time_random = time.time()

    # Calcula e imprime o tempo de execução para o array aleatório
    execution_time_random = end_time_random - start_time_random
    print(f"Tamanho do array aleatório: {size}, Tempo de execução: {execution_time_random} segundos")

if __name__ == "__main__":
    main()
