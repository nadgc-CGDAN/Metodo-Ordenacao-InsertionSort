import matplotlib.pyplot as plt
import numpy as np

# Dados
algorithms = ['Insertion Sort (10^6)', 'Heap Sort (10^7)']
times = [1249.0390, 27.4192]

# Criar o gráfico
plt.figure(figsize=(12, 7))
bars = plt.bar(algorithms, times, color=['blue', 'green'])

# Adicionar linha de destaque para Heap Sort
plt.axhline(y=27.4192, color='red', linestyle='--', label='Heap Sort')

# Adicionar rótulos e título
plt.xlabel('Algoritmo')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Comparação de Tempo de Execução entre Insertion Sort e Heap Sort')

# Adicionar a legenda
plt.legend(loc='upper right')

# Adicionar anotações para destacar os tempos
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', 
             ha='center', va='bottom', color='black')

# Ajustar o formato do eixo y para evitar notação científica
plt.ticklabel_format(axis='y', style='plain')

# Adicionar grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Exibir o gráfico
plt.show()
