def ordenacao_por_selecao(arr):
    novo_arr = []
    
    for i in range(len(arr)):
        # pega indice do menor elemento do array 
        indice_menor_elemento = busca_indice_do_menor_elemento(arr) 
        # retorna o menor elemento do array removendo-o do array original usando 'pop'
        menor_elemento = arr.pop(indice_menor_elemento) 
        # adiciona o menor elemento no array auxiliar
        novo_arr.append(menor_elemento) 
    
    return novo_arr


def busca_indice_do_menor_elemento(arr):
    menor_elemento = arr[0]
    indice_menor_elemento = 0
    for i in range(1, len(arr)):
        if arr[i] < menor_elemento:
            menor_elemento = arr[i]
            indice_menor_elemento = i
        
    return indice_menor_elemento

