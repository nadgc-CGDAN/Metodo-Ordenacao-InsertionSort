import time
import random

def insertion_sort(array):
    """Ordena um array usando o algoritmo Insertion Sort em ordem decrescente."""
    n = len(array)
    comparacoes = 0  # Contador para comparações
    trocas = 0       # Contador para trocas
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] < key:
            comparacoes += 1  # Incrementa o contador de comparações
            array[j + 1] = array[j]
            j -= 1
            trocas += 1  # Incrementa o contador de trocas
        array[j + 1] = key
        if j >= 0:  # Para a última comparação que não resultou em troca
            comparacoes += 1
    return array, comparacoes, trocas

def generate_large_array(size):
    """Gera um array de tamanho 'size' com números aleatórios."""
    return [random.randint(1, 1000000) for _ in range(size)]

def main():
    """Função principal que executa o programa."""
    arrays = {
        "Exemplo": [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24],
        "10^7": generate_large_array(10**7),
        "10^8": generate_large_array(10**8)
    }

    for name, array in arrays.items():
        # Imprime o array original
        print(f"\nArray original ({name}):")
        print(array[:10], "...")  # Mostra apenas os primeiros 10 elementos para arrays grandes

        # Inicia a contagem de tempo
        start_time = time.time()

        # Ordena o array usando o insertion sort e obtém contagem de comparações e trocas
        sorted_array, comparacoes, trocas = insertion_sort(array)

        # Finaliza a contagem de tempo
        end_time = time.time()

        # Imprime o array ordenado
        print(f"Array ordenado ({name}):")
        print(sorted_array[:10], "...")  # Mostra apenas os primeiros 10 elementos para arrays grandes

        # Imprime o número de comparações e trocas realizadas
        print("Número de comparações:", comparacoes)
        print("Número de trocas:", trocas)

        # Análise assintótica
        print("Análise assintótica:")
        print("Número de comparações no pior caso: O(n^2)")
        print("Número de trocas no pior caso: O(n^2)")

        # Calcula e imprime o tempo de execução
        execution_time = end_time - start_time
        print("Tempo de execução:", execution_time, "segundos")

if __name__ == "__main__":
    main()
