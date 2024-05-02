import time

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
                print(f"Iteração {i+1}, Comparação {comparacoes}: Troca {array[j+1]} com {array[j]}: {array}")
                if j+2 < n:
                    comparacoes += 1  # Incrementa o contador de comparações
                    if array[j+1] < array[j+2]:
                        array[j+1], array[j+2] = array[j+2], array[j+1]
                        trocas += 1  # Incrementa o contador de trocas
                        print(f"Iteração {i+1}, Comparação {comparacoes}: Troca {array[j+2]} com {array[j+1]}: {array}")
    return array, comparacoes, trocas

def main():
    """Função principal que executa o programa."""
    array = [31, 14, 23, 37, 11, 26, 16, 9, 47, 30, 33, 24]  # Array de exemplo

    # Imprime o array original
    print("Array original:")
    print(array)

    # Inicia a contagem de tempo
    start_time = time.time()

    # Ordena o array usando o bubble sort e obtém contagem de comparações e trocas
    sorted_array, comparacoes, trocas = bubble_sort(array)

    # Finaliza a contagem de tempo
    end_time = time.time()

    # Imprime o array ordenado
    print("Array ordenado:")
    print(sorted_array)

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
