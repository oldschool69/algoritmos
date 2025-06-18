from selection_sort import ordenacao_por_selecao
from quick_sort import quicksort
from grafo_dfs import dfs
from busca_binaria import busca_binaria

             

def main():
    print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 3))
    print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 33))
    print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 1))
    print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 8))
    print(busca_binaria([3], 3))
    print(busca_binaria([3], 33))
    print(busca_binaria([], 3))
    

if __name__ == "__main__":
    main()
