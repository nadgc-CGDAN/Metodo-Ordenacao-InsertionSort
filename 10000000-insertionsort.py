import time
import random

def heapify(array, n, i, comparacoes, trocas):
    """Mantém a propriedade de heap para um subárvore enraizada no índice i."""
    maior = i  # Inicializa o maior como raiz
    esquerda = 2 * i + 1  # Filho à esquerda
    direita = 2 * i + 2  # Filho à direita

    # Se o filho à esquerda do nó raiz existe e é maior que a raiz
    if esquerda < n and array[esquerda] < array[maior]:
        maior = esquerda
        comparacoes += 1

    # Se o filho à direita do nó raiz existe e é maior que o maior até agora
    if direita < n and array[direita] < array[maior]:
        maior = direita
        comparacoes += 1

    # Se o maior não é a raiz
    if maior != i:
        array[i], array[maior] = array[maior], array[i]  # Troca
        trocas += 1

        # Heapify o subárvore afetada
        comparacoes, trocas = heapify(array, n, maior, comparacoes, trocas)

    return comparacoes, trocas

def heapsort(array):
    """Ordena um array usando o algoritmo Heapsort."""
    n = len(array)
    comparacoes = 0  # Contador para comparações
    trocas = 0       # Contador para trocas

    # Constrói um maxheap
    for i in range(n // 2 - 1, -1, -1):
        comparacoes, trocas = heapify(array, n, i, comparacoes, trocas)

    # Extrai elementos um a um da heap
    for i in range(n-1, 0, -1):
        # Move a raiz atual para o final
        array[i], array[0] = array[0], array[i]
        trocas += 1

        # Chama heapify na heap reduzida
        comparacoes, trocas = heapify(array, i, 0, comparacoes, trocas)

    return array, comparacoes, trocas

def main():
    """Função principal que executa o programa."""
    # Array de exemplo com os valores fornecidos
    array_example = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]

    # Inicia a contagem de tempo para o array de exemplo
    start_time_example = time.time()

    # Ordena o array de exemplo em ordem decrescente usando o heapsort
    sorted_array_example, comparacoes_example, trocas_example = heapsort(array_example.copy())

    # Finaliza a contagem de tempo para o array de exemplo
    end_time_example = time.time()

    # Imprime o array de exemplo ordenado em ordem decrescente
    print("Array de exemplo ordenado em ordem decrescente:")
    print(sorted_array_example)

    # Imprime o número de comparações e trocas realizadas para o array de exemplo
    print("Numero de comparacoes para o array de exemplo:", comparacoes_example)
    print("Numero de trocas para o array de exemplo:", trocas_example)

    # Calcula e imprime o tempo de execução para o array de exemplo
    execution_time_example = end_time_example - start_time_example
    print(f"Tempo de execucao para o array de exemplo: {execution_time_example:.6f} segundos")

    # Gera um array aleatório de tamanho 10^7
    size = 10**7
    array_large = random.choices(array_example, k=size)

    # Inicia a contagem de tempo para o array grande
    start_time_large = time.time()

    # Ordena o array grande em ordem decrescente usando o heapsort
    sorted_array_large, comparacoes_large, trocas_large = heapsort(array_large.copy())

    # Finaliza a contagem de tempo para o array grande
    end_time_large = time.time()

    # Calcula e imprime o tempo de execução para o array grande
    execution_time_large = end_time_large - start_time_large
    print(f"Tamanho do array grande: {size}, Tempo de execucao: {execution_time_large:.6f} segundos")

    # Imprime uma amostra do array grande ordenado em ordem decrescente
    print("Amostra do array grande ordenado em ordem decrescente:")
    print(sorted_array_large[:10])

if __name__ == "__main__":
    main()
