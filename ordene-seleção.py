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
    return array, comparacoes, trocas

def main():
    """Função principal que executa o programa."""
    size = 10**7  # Tamanho do array
    array = [random.randint(0, 100) for _ in range(size)]  # Gera um array aleatório de tamanho 10^7

    # Inicia a contagem de tempo
    start_time = time.time()

    # Ordena o array usando o bubble sort e obtém contagem de comparações e trocas
    sorted_array, comparacoes, trocas = bubble_sort(array)

    # Finaliza a contagem de tempo
    end_time = time.time()

    # Calcula e imprime o tempo de execução
    execution_time = end_time - start_time
    print(f"Tamanho do array: {size}, Tempo de execução: {execution_time} segundos")
    print("Número de comparações:", comparacoes)
    print("Número de trocas:", trocas)

if __name__ == "__main__":
    main()