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
    size = 10**8  # Tamanho do array aleatório

    # Para tamanhos muito grandes, a criação do array pode ser muito lenta
    # ou causar problemas de memória. Ajuste conforme necessário.
    
    # Para evitar problemas, vamos gerar apenas uma amostra menor para o array aleatório
    array_sample_size = 10**5  # Tamanho reduzido para a amostra
    array = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24] * (array_sample_size // 12)
    
    # Gera um array aleatório de tamanho reduzido com os mesmos valores do array de exemplo
    array_random = array[:]

    # Inicia a contagem de tempo para o array de exemplo
    start_time_example = time.time()

    # Ordena o array de exemplo em ordem decrescente usando o insertion sort
    sorted_array_example, comparacoes_example, trocas_example = insertion_sort(array.copy())

    # Finaliza a contagem de tempo para o array de exemplo
    end_time_example = time.time()

    # Imprime uma amostra do array de exemplo ordenado
    print("Amostra do array de exemplo ordenado:")
    print(sorted_array_example[:10])

    # Imprime o número de comparações e trocas realizadas para o array de exemplo
    print("Número de comparações para o array de exemplo:", comparacoes_example)
    print("Número de trocas para o array de exemplo:", trocas_example)

    # Calcula e imprime o tempo de execução para o array de exemplo
    execution_time_example = end_time_example - start_time_example
    print(f"Tamanho do array de exemplo: {len(array)}, Tempo de execução: {execution_time_example:.6f} segundos")

    # Inicia a contagem de tempo para o array aleatório
    start_time_random = time.time()

    # Ordena o array aleatório em ordem decrescente usando o insertion sort
    sorted_array_random, comparacoes_random, trocas_random = insertion_sort(array_random.copy())

    # Finaliza a contagem de tempo para o array aleatório
    end_time_random = time.time()

    # Calcula e imprime o tempo de execução para o array aleatório
    execution_time_random = end_time_random - start_time_random
    print(f"Tamanho do array aleatório: {array_sample_size}, Tempo de execução: {execution_time_random:.6f} segundos")

    # Imprime uma amostra do array aleatório ordenado em ordem decrescente
    print("Amostra do array aleatório ordenado em ordem decrescente:")
    print(sorted_array_random[:10])

if __name__ == "__main__":
    main()
