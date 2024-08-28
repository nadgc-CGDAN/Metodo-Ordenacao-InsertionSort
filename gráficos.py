'''10^4'''
'''
import time
import random
import matplotlib.pyplot as plt

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
    # Array de exemplo fornecido
    array_example = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]
    size = 10**4
    num_executions = 10  # Número de execuções para o tamanho fixo

    # Armazenamento dos resultados para o array de exemplo
    example_times = []
    example_comparacoes_totais = []
    example_trocas_totais = []

    # Executa a ordenação para o array de exemplo
    start_time_example = time.time()
    _, comparacoes_example, trocas_example = insertion_sort(array_example.copy())
    end_time_example = time.time()
    example_times.append(end_time_example - start_time_example)
    example_comparacoes_totais.append(comparacoes_example)
    example_trocas_totais.append(trocas_example)

    # Armazenamento dos resultados para o array aleatório
    random_times = []
    random_comparacoes_totais = []
    random_trocas_totais = []

    for _ in range(num_executions):
        # Gera um array aleatório de tamanho especificado
        array_random = [random.randint(0, 100) for _ in range(size)]

        # Inicia a contagem de tempo
        start_time_random = time.time()

        # Ordena o array aleatório em ordem decrescente usando o insertion sort
        _, comparacoes_random, trocas_random = insertion_sort(array_random.copy())

        # Finaliza a contagem de tempo
        end_time_random = time.time()

        # Calcula e armazena o tempo de execução, comparações e trocas
        execution_time = end_time_random - start_time_random
        random_times.append(execution_time)
        random_comparacoes_totais.append(comparacoes_random)
        random_trocas_totais.append(trocas_random)

    # Geração dos gráficos
    plt.figure(figsize=(18, 6))

    # Gráfico de Tempo de Execução
    plt.subplot(1, 3, 1)
    plt.bar(['Array de Exemplo', 'Array Aleatório'], [example_times[0], sum(random_times)/num_executions], color=['b', 'r'])
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Tempo de Execução')

    # Gráfico de Comparações
    plt.subplot(1, 3, 2)
    plt.bar(['Array de Exemplo', 'Array Aleatório'], [example_comparacoes_totais[0], sum(random_comparacoes_totais)/num_executions], color=['b', 'r'])
    plt.ylabel('Número de Comparações')
    plt.title('Comparações')

    # Gráfico de Trocas
    plt.subplot(1, 3, 3)
    plt.bar(['Array de Exemplo', 'Array Aleatório'], [example_trocas_totais[0], sum(random_trocas_totais)/num_executions], color=['b', 'r'])
    plt.ylabel('Número de Trocas')
    plt.title('Trocas')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


















'''10^5'''

''' '''
import time
import random
import matplotlib.pyplot as plt

def insertion_sort(array):
    """Ordena um array usando o algoritmo Insertion Sort."""
    n = len(array)
    for i in range(1, n):
        chave = array[i]
        j = i - 1
        # Move os elementos do array que são maiores que a chave para uma posição à frente
        while j >= 0 and array[j] < chave:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave
    return array

def main():
    """Função principal que executa o programa."""
    # Array fornecido
    array_provided = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]

    # Tamanhos dos arrays para análise
    sizes = [10**2, 10**3, 10**4, 10**5]

    # Listas para armazenar tempos de execução
    execution_times = []

    # Medição do tempo de execução para diferentes tamanhos de arrays
    for size in sizes:
        # Gera um array aleatório de tamanho especificado
        array_random = [random.randint(0, 100) for _ in range(size)]

        # Inicia a contagem de tempo para o array aleatório
        start_time = time.time()

        # Ordena o array aleatório em ordem decrescente usando o insertion sort
        insertion_sort(array_random.copy())

        # Finaliza a contagem de tempo para o array aleatório
        end_time = time.time()

        # Calcula e armazena o tempo de execução para o array aleatório
        execution_time = end_time - start_time
        execution_times.append(execution_time)

        print(f"Tamanho do array: {size}, Tempo de execução: {execution_time} segundos")

    # Ordena o array fornecido em ordem decrescente
    sorted_array_provided = insertion_sort(array_provided.copy())

    # Imprime o array fornecido ordenado
    print("Array fornecido ordenado em ordem decrescente:")
    print(sorted_array_provided)

    # Plotagem do gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, execution_times, marker='o', linestyle='-', color='b')
    plt.title('Tempo de Execução do Insertion Sort para Diferentes Tamanhos de Arrays')
    plt.xlabel('Tamanho do Array')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.grid(True)
    plt.xscale('log')  # Escala logarítmica para o eixo x
    plt.yscale('log')  # Escala logarítmica para o eixo y (opcional, dependendo dos tempos)
    plt.show()

if __name__ == "__main__":
    main()
''' ''' 


