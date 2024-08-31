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
    return array, comparacoes, trocas

def main():
    """Função principal que executa o programa."""
    # Array fornecido
    array = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]

    # Gera um array aleatório de tamanho 10^5
    size = 10**5
    array_random = [random.randint(0, 100) for _ in range(size)]

    # Inicia a contagem de tempo para o array aleatório
    start_time_random = time.time()

    # Ordena o array aleatório em ordem decrescente usando o insertion sort
    sorted_array_random, comparacoes_random, trocas_random = insertion_sort(array_random.copy())

    # Finaliza a contagem de tempo para o array aleatório
    end_time_random = time.time()

    # Calcula e imprime o tempo de execução para o array aleatório
    execution_time_random = end_time_random - start_time_random
    print(f"Tamanho do array aleatorio: {size}, Tempo de execucao: {execution_time_random} segundos")

    # Ordena o array fornecido em ordem decrescente
    sorted_array_example, _, _ = insertion_sort(array.copy())

    # Imprime o array fornecido ordenado
    print("Array fornecido ordenado em ordem decrescente:")
    print(sorted_array_example)

if __name__ == "__main__":
    main()
