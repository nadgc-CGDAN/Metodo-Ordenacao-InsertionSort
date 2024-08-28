import time

def heapify(array, n, i):
    """Converte um subarray em um heap máximo."""
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heap_sort(array):
    """Ordena um array usando o algoritmo Heap Sort."""
    n = len(array)
    comparacoes = 0
    trocas = 0

    # Construa um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extraia elementos um a um do heap
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        trocas += 1
        heapify(array, i, 0)
    
    return array, comparacoes, trocas

def main():
    """Função principal que executa o programa."""
    size = 10**8  # Ajustado para um tamanho muito grande
    sample_array = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]
    
    # Gera um array aleatório de tamanho 10^8 replicando o array de exemplo
    array = sample_array * (size // len(sample_array))

    # Inicia a contagem de tempo para o array aleatório
    start_time = time.time()

    # Ordena o array aleatório usando o Heap Sort
    sorted_array, comparacoes, trocas = heap_sort(array.copy())

    # Finaliza a contagem de tempo para o array aleatório
    end_time = time.time()

    # Calcula e imprime o tempo de execução para o array aleatório
    execution_time = end_time - start_time
    print(f"Tamanho do array: {size}, Tempo de execucao: {execution_time:.6f} segundos")

    # Imprime uma amostra do array aleatório ordenado
    print("Amostra do array aleatorio ordenado:")
    print(sorted_array[:10])

if __name__ == "__main__":
    main()
