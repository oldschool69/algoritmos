from selection_sort import ordenacao_por_selecao
from quick_sort import quicksort
from grafo_dfs import dfs
from busca_binaria import busca_binaria
from dijkstra import dijkstra
from greed_melhores_estacoes_radio import localizar_melhores_estacoes
from programacao_dinamica import problema_da_mochila, knapsack
             

def main():
    # print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 3))
    # print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 33))
    # print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 1))
    # print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 8))
    # print(busca_binaria([3], 3))
    # print(busca_binaria([3], 33))
    # print(busca_binaria([], 3))
    # dijkstra()
    # localizar_melhores_estacoes()
    
    problema_da_mochila()
    

if __name__ == "__main__":
    main()
