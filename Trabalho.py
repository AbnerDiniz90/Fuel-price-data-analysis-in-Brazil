import pandas as pd
import time
import matplotlib.pyplot as plt

arq = pd.read_csv('Precos.csv', delimiter=';', decimal=',', encoding='utf-8')

MINIMUM= 32

def ini_dados(produto : str, estado : str) -> list:

    df_filtered = arq.loc[(arq['Produto'] == produto) & (arq['Estado - Sigla'] == estado)]

    valores = [row['Valor de Venda'] for _, row in df_filtered.iterrows()]
    return valores 
  
def timsort(arr):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]

    def find_runs(arr):
        runs = []
        n = len(arr)
        i = 0
        while i < n:
            run = [arr[i]]
            j = i + 1
            while j < n:     
                if arr[j] >= arr[j-1]:
                    run.append(arr[j])
                else:
                    break
                j += 1
            runs.append(run)
            i = j
        return runs

    runs = find_runs(arr)
    while len(runs) > 1:
        merged_runs = []
        for i in range(0, len(runs), 2):
            left = runs[i]
            right = runs[i+1] if i+1 < len(runs) else []
            merged_runs.append(merge(left, right))
        runs = merged_runs

    return runs[0]

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def create_graph(produto, estados):
    estados_list = []
    max_valores = []
    min_valores = []
    mean_valores = []

    for estado, valores in estados.items():
        estados_list.append(estado)

        valores = timsort(valores)
        
        max_valores.append((valores[-1]))
        min_valores.append((valores[0]))
        soma = sum(valores)
        media = soma / len(valores)
        mean_valores.append(media)

    plt.figure(figsize=(12, 6))
    plt.plot(estados_list, max_valores, 'r-o', label='Máximo', linewidth=2)
    plt.plot(estados_list, min_valores, 'g-o', label='Mínimo', linewidth=2)
    plt.plot(estados_list, mean_valores, 'b-o', label='Média', linewidth=2)
    plt.title(f'Análise de Preços - {produto}')
    plt.xlabel('Estados')
    plt.ylabel('Preço (R$)')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    plt.close()

produtos_dict = {
    produto: {
        estado: ini_dados(produto, estado)
        for estado in timsort(list(arq[arq['Produto'] == produto]['Estado - Sigla'].unique()))
    }
    for produto in arq['Produto'].unique()
}

start_time = time.time()

for produto, estados in produtos_dict.items():
    print(f"\nProduto: {produto}")
    create_graph(produto, estados)

    for estado, valores in estados.items():
        valores.sort()
        print(f"{estado}: {valores[:5]}")

fim = time.time()

print(f"Tempo de execucao: {fim - start_time} segundos")