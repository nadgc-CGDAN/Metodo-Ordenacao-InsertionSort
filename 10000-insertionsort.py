import time
import random

def insertion_sort(array):
    """Ordena um array usando o algoritmo Insertion Sort."""
    n = len(array)
    comparacoes = 0  # Contador para comparações
    trocas = 0       # Contador para trocas
    for i in range(1, n):
        chave = array[i]
        j = i - 1
        # Move os elementos do array que são maiores que a chave para uma posição à frente
        while j >= 0 and array[j] < chave:
            comparacoes += 1  # Incrementa o contador de comparações
            array[j + 1] = array[j]
            trocas += 1       # Incrementa o contador de trocas
            j -= 1
        comparacoes += 1  # Conta a última comparação onde array[j] <= chave
        array[j + 1] = chave
        print(f"Iteração {i}: {array}")  # Mostra o array após cada iteração
    return array, comparacoes, trocas

def main():
    """Função principal que executa o programa."""
    # Array de exemplo fornecido
    array = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]

    # Tamanho do array aleatório
    size = 10**4

    # Gera um array aleatório de tamanho 10^4
    array_random = [random.randint(0, 100) for _ in range(size)]

    # Inicia a contagem de tempo para o array de exemplo
    start_time_example = time.time()

    # Ordena o array de exemplo em ordem decrescente usando o insertion sort
    sorted_array_example, comparacoes_example, trocas_example = insertion_sort(array.copy())

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
    print(f"Tamanho do array de exemplo: {len(array)}, Tempo de execucao: {execution_time_example} segundos")

    # Inicia a contagem de tempo para o array aleatório
    start_time_random = time.time()

    # Ordena o array aleatório em ordem decrescente usando o insertion sort
    sorted_array_random, comparacoes_random, trocas_random = insertion_sort(array_random.copy())

    # Finaliza a contagem de tempo para o array aleatório
    end_time_random = time.time()

    # Calcula e imprime o tempo de execução para o array aleatório
    execution_time_random = end_time_random - start_time_random
    print(f"Tamanho do array aleatorio: {size}, Tempo de execucao: {execution_time_random} segundos")

if __name__ == "__main__":
    main()
