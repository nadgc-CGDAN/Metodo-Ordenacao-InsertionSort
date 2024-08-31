import time

def heapify(array, n, i):
    """Converte um subarray em um heap mínimo."""
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] > array[l]:
        smallest = l

    if r < n and array[smallest] > array[r]:
        smallest = r

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, n, smallest)

def heap_sort(array):
    """Ordena um array em ordem decrescente usando o algoritmo Heap Sort."""
    n = len(array)

    # Construa um heap mínimo
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extraia elementos um a um do heap e coloque no final do array
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)
    
    # Inverter o array para que ele fique em ordem decrescente
    array.reverse()
    return array

def main():
    """Função principal que executa o programa."""
    size = 10**8  # Tamanho do array
    sample_array = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]
    
    # Gera um array aleatório de tamanho 10^8 replicando o array de exemplo
    array = sample_array * (size // len(sample_array))

    # Inicia a contagem de tempo para a ordenação
    start_time = time.time()

    # Ordena o array usando o Heap Sort em ordem decrescente
    sorted_array = heap_sort(array.copy())

    # Finaliza a contagem de tempo
    end_time = time.time()

    # Calcula e imprime o tempo de execução
    execution_time = end_time - start_time
    print(f"Tamanho do array: {size}, Tempo de execucao: {execution_time:.6f} segundos")

    # Imprime uma amostra do array ordenado em ordem decrescente
    print("Amostra do array ordenado em ordem decrescente:")
    print(sorted_array[:12])

if __name__ == "__main__":
    main()
