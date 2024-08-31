import time
import random

def heapify(array, n, i):
    """Transforma um subárvore em um heap."""
    largest = i  # Inicialmente, o maior é a raiz
    left = 2 * i + 1  # Índice do filho esquerdo
    right = 2 * i + 2  # Índice do filho direito

    # Verifica se o filho esquerdo existe e é maior que a raiz
    if left < n and array[left] > array[largest]:
        largest = left

    # Verifica se o filho direito existe e é maior que o maior até agora
    if right < n and array[right] > array[largest]:
        largest = right

    # Se o maior não for a raiz
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # Troca
        heapify(array, n, largest)  # Recursivamente transforma o subárvore afetado em um heap

def heapsort(array):
    """Ordena um array em ordem decrescente usando o algoritmo Heapsort."""
    n = len(array)
    
    # Constrói um heap (rearranja o array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    
    # Extrai um elemento por vez do heap
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]  # Move a raiz para o fim
        heapify(array, i, 0)  # Chama heapify no heap reduzido

    # Reversão final para obter ordem decrescente
    array.reverse()

def main():
    """Função principal que executa o programa."""
    size = 10**8  # Tamanho do array aleatório

    # Array de exemplo com valores predefinidos
    array_example = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]

    # Gera um array aleatório de tamanho 10^8 com os mesmos valores do array de exemplo
    array_random = random.choices(array_example, k=size)

    # Inicia a contagem de tempo para o array de exemplo
    start_time_example = time.time()

    # Ordena o array de exemplo em ordem decrescente usando o heapsort
    sorted_array_example = array_example.copy()
    heapsort(sorted_array_example)

    # Finaliza a contagem de tempo para o array de exemplo
    end_time_example = time.time()

    # Imprime o array de exemplo ordenado
    print("Array de exemplo ordenado em ordem decrescente:")
    print(sorted_array_example)

    # Calcula e imprime o tempo de execução para o array de exemplo
    execution_time_example = end_time_example - start_time_example
    print(f"Tempo de execucao para o array de exemplo: {execution_time_example:.6f} segundos")

    # Inicia a contagem de tempo para o array aleatório
    start_time_random = time.time()

    # Ordena o array aleatório em ordem decrescente usando o heapsort
    sorted_array_random = array_random.copy()
    heapsort(sorted_array_random)

    # Finaliza a contagem de tempo para o array aleatório
    end_time_random = time.time()

    # Calcula e imprime o tempo de execução para o array aleatório
    execution_time_random = end_time_random - start_time_random
    print(f"Tamanho do array aleatorio: {size}, Tempo de execucao: {execution_time_random:.6f} segundos")

    # Imprime uma amostra do array aleatório ordenado em ordem decrescente
    print("Amostra do array aleatorio ordenado em ordem decrescente:")
    print(sorted_array_random[:10])

if __name__ == "__main__":
    main()
